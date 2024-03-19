import pandas as pd

sourcefile = 'config/regional_code.xlsx'
df = pd.read_excel(sourcefile, index_col=0)
dic = df.to_dict(orient='dict')
regional_dict = dic['regional_name']

SERVICE_KEY = "qe6V6jR%2BqQ26NbratsNZm0OyGKQP8T5Kt3I5WbvDR7SzNErWuh%2FzXY5pftqTzQetGlq2gCXazL%2B8bn%2BMYvk%2BVA%3D%3D"
META_DICT = {
                "아파트": {
                    "매매": { ##2024/02/25 '동',''등기일자','매도자','매수자' 추가
                        "url": "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev",
                        "columns": ['지역코드', '도로명', '법정동', '지번', '아파트', '건축년도', '층', '전용면적', '년', '월', '일', '거래금액', '도로명건물본번호코드', '도로명건물부번호코드', '도로명시군구코드', '도로명일련번호코드', '도로명지상지하코드', '도로명코드', '법정동본번코드', '법정동부번코드', '법정동시군구코드', '법정동읍면동코드', '법정동지번코드', '일련번호', '거래유형', '중개사소재지', '해제사유발생일', '해제여부','동','등기일자','매수자','매도자'],
                        "eng_columns" : ['regional_code','road_name','dong','jibun','apartment_name','build_year','floor','area_of_exclusive_use','deal_year','deal_month','deal_day','deal_amount','road_name_bonbun','road_name_bubun','road_name_sigungu_code','road_name_seq','road_name_basement_code','road_name_code','bonbun','bubun','sigungu_code','eubmyundong_code','land_code','ilryun_code','req_gbn','rdealer_lawdnm','cancel_del_day','cancel_deal_type','apartment_dong','registeration_date','buyer_gbn','seller_gbn']
                    },
                    "전월세": {
                        "url": "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptRent",
                        "columns": ['지역코드', '법정동', '지번', '아파트', '건축년도', '층', '전용면적', '년', '월', '일', '보증금액', '월세금액', '계약구분', '계약기간', '갱신요구권사용', '종전계약보증금', '종전계약월세']
                    },
                },
                "오피스텔": {
                    "매매": {
                        "url": "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcOffiTrade",
                        "columns": ['지역코드', '시군구', '법정동', '지번', '단지', '건축년도', '층', '전용면적', '년', '월', '일', '거래금액', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                    },
                    "전월세": {
                        "url": "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcOffiRent",
                        "columns": ['지역코드', '시군구', '법정동', '지번', '단지', '건축년도', '층', '전용면적', '년', '월', '일', '보증금', '월세', '계약구분', '계약기간', '갱신요구권사용', '종전계약보증금', '종전계약월세']
                    },
                },
                "분양입주권": {
                    "매매": {
                        "url": "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSilvTrade",
                        "columns": ['지역코드', '시군구', '법정동', '지번', '단지', '층', '전용면적', '구분', '년', '월', '일', '거래금액', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                    },
                },
}
