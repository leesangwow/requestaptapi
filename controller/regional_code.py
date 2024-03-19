import pandas as pd
from app.models import RegionalInfo
from app import db

class InitRegionalCode:

    regional_dict = {}
        
    def load_table(self):
        regional_list = RegionalInfo.query.order_by(RegionalInfo.regional_name)
        for regional in regional_list:
            self.regional_dict[regional.regional_code] = regional.regional_name

        return self.regional_dict
    
    def update_table(self):
        if self.regional_dict:
            for code, name in self.regional_dict.items():
                r = RegionalInfo(
                    regional_code = code,
                    regional_name = name
                )
                db.session.add(r)
            db.session.commit()
    
    def load_new_soucre(self, sourcefile):
        df = pd.read_excel(sourcefile, index_col=0)
        dic = df.to_dict(orient='dict')
        self.regional_dict = dic['regional_name']

