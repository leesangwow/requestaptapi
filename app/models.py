from app import db

class Task(db.Model):
    __tablename__ = "test_table"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))

class RegionalInfo(db.Model):
    __tablename__ = "regional_tb"
    regional_code = db.Column(db.Integer, primary_key=True)
    regional_name = db.Column(db.String(50), nullable=False)

class Aptmm(db.Model):
    __tablename__ = "apt_mm_tb"
    id                  = db.Column(db.Integer, primary_key=True)
    regional_code       = db.Column(db.Integer, nullable=False)
    # regional_code       = db.Column(db.Integer, db.ForeignKey('regional_tb.regional_code'), nullable=False)
    # regional_info       = db.relationship('RegionalInfo', backref=db.backref('aptmm_set'))
    road_name           = db.Column(db.String(100), nullable=False)
    dong                = db.Column(db.String(50), nullable=False)
    jibun               = db.Column(db.String(50))
    apartment_name      = db.Column(db.String(100), nullable=False)
    build_year          = db.Column(db.Integer, nullable=False)
    floor               = db.Column(db.Integer, nullable=False)
    area_of_exclusive_use = db.Column(db.Float, nullable=False)
    deal_year           = db.Column(db.Integer, nullable=False)
    deal_month          = db.Column(db.Integer, nullable=False)
    deal_day            = db.Column(db.Integer, nullable=False)
    deal_amount         = db.Column(db.String(100), nullable=False)
    road_name_bonbun    = db.Column(db.String(30))
    road_name_bubun     = db.Column(db.String(30))
    road_name_sigungu_code = db.Column(db.String(50))
    road_name_seq       = db.Column(db.String(50))
    road_name_basement_code = db.Column(db.String(50))
    road_name_code      = db.Column(db.String(50))
    bonbun              = db.Column(db.String(50))
    bubun               = db.Column(db.String(50))
    sigungu_code        = db.Column(db.Integer, nullable=False)
    eubmyundong_code    = db.Column(db.String(100))
    land_code           = db.Column(db.String(100))
    ilryun_code         = db.Column(db.String(100))
    req_gbn             = db.Column(db.String(100))
    rdealer_lawdnm      = db.Column(db.String(100))
    cancel_deal_day      = db.Column(db.String(30))
    cancel_deal_type    = db.Column(db.String(30))
    apartment_dong      = db.Column(db.String(50))
    registeration_date  = db.Column(db.String(30))
    buyer_gbn           = db.Column(db.String(30))
    seller_gbn          = db.Column(db.String(30))