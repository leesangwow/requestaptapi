from config import metadata
import os, requests
from dotenv import load_dotenv
import pandas as pd
import xmltodict
from app.models import Aptmm
from app import db

service_key = metadata.SERVICE_KEY
api_url = metadata.META_DICT.get("아파트").get("매매").get("url")
api_columns = metadata.META_DICT.get("아파트").get("매매").get("columns")


def get_data(LAWD_CD, DEAL_YMD):

    #Base Dataframe
    df = pd.DataFrame(columns=api_columns)

    #API 요청 PARAMETERS
    params ={'serviceKey' : requests.utils.unquote(service_key), 
                'pageNo' : '1', 
                'numOfRows' : '99999', 
                'LAWD_CD' : LAWD_CD, 
                'DEAL_YMD' : DEAL_YMD }
    #API 요청 후 json 변환
    res = requests.get(api_url,params=params)
    res_json = xmltodict.parse(res.text)

    #응답의 resultCode가 00이 아니면 ERROR
    if res_json['response']['header']['resultCode'] != '00': 
        error_message = res_json['response']['header']['resultMsg']
        raise Exception(error_message)
    
    #응답의 Body에서 items만 추출
    items = res_json['response']['body']['items']

    #아이템이 하나도 없으면 빈 Dataframe 반환
    if not items:
        return pd.DataFrame(columns=api_columns)
    data = items['item']

    if isinstance(data, list):
        sub = pd.DataFrame(data)
    elif isinstance(data, dict):
        sub = pd.DataFrame([data])

    df = pd.concat([df, sub], axis=0, ignore_index=True)

    return df   

def upload_aptmm(df):

    r = 0
    for idx, row in df.iterrows():
        t = Aptmm(
        regional_code = row['지역코드'],
        road_name = row['도로명'],
        dong = row['법정동'],
        jibun               = row['지번'],
        apartment_name      = row['아파트'],
        build_year          = row['건축년도'],
        floor               = row['층'],
        area_of_exclusive_use = row['전용면적'],
        deal_year           = row['년'],
        deal_month          = row['월'],
        deal_day            = row['일'],
        deal_amount         = row['거래금액'],
        road_name_bonbun    = row['도로명건물본번호코드'],
        road_name_bubun     = row['도로명건물부번호코드'],
        road_name_sigungu_code = row['도로명시군구코드'],
        road_name_seq       = row['도로명일련번호코드'],
        road_name_basement_code = row['도로명지상지하코드'],
        road_name_code      = row['도로명코드'],
        bonbun              = row['법정동본번코드'],
        bubun               = row['법정동부번코드'],
        sigungu_code        = row['법정동시군구코드'],
        eubmyundong_code    = row['법정동읍면동코드'],
        land_code           = row['법정동지번코드'],
        ilryun_code         = row['일련번호'],
        req_gbn             = row['거래유형'],
        rdealer_lawdnm      = row['중개사소재지'],
        cancel_deal_day      = row['해제사유발생일'],
        cancel_deal_type    = row['해제여부'],
        apartment_dong      = row['동'],
        registeration_date  = row['등기일자'],
        buyer_gbn           = row['매수자'],
        seller_gbn          = row['매도자']
        )
        db.session.add(t)
        r += 1
    db.session.commit()
    return "Successfully Upload : ", r