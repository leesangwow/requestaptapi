from flask import Blueprint, request, render_template
from config import metadata
from controller import api_archive, regional_code
from controller.regional_code import InitRegionalCode
import pandas as pd
import app.models as models
import xmltodict

bp = Blueprint('main', __name__, url_prefix='/')
#regional_dict = metadata.regional_dict

@bp.route('/getapi',methods=['GET','POST'])
def getapi():

    region_info = InitRegionalCode()
    regional_dict = region_info.load_table()
    regional_name_list = regional_dict.values()
    city_name_set = set([str(city).split(' ')[0] for city in regional_name_list])
    city_name_list = sorted(list(city_name_set))

    if not regional_dict:
        print("load new data")
        region_info.load_new_soucre('config/regional_code.xlsx') 
        region_info.update_table()
    regional_dict = region_info.load_table()

    if request.method =='GET':
        return render_template("index.html", result ='ready',regional_dict=regional_dict, city_name_list=city_name_list, df=pd.DataFrame())
    else:
        LAWD_CD = request.form['sigungu_code']
        DEAL_YMD = request.form['deal_date']
        df = api_archive.get_data(LAWD_CD, DEAL_YMD)
        result_msg = api_archive.upload_aptmm(df)

        return render_template("index.html", df=df,regional_dict=regional_dict, city_name_list=city_name_list, result_msg=result_msg)
    
@bp.route('/')
def index():
    
    return 'Pybo index'