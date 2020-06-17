from flask import Flask,render_template,request, redirect, make_response, url_for, session
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  Column, Integer, String, MetaData, DateTime, func
from sqlalchemy.sql import text
app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///project.db'
db= SQLAlchemy(app)
def getApp():    
 return app 
#database

class logins_data (db.Model): 
   Id= Column(db.Integer, primary_key = True ,autoincrement = True)
   Username= Column(db.String, nullable=False) 
   Password= Column( db.String, nullable=False)
   BlockName= Column( db.String, nullable=False)
   AccessType= Column(db.String, nullable=False)
   DateTime= Column(db.DateTime, default=datetime.utcnow)
   def __repr__(self):
        return "Id %r"  % self.Id

class logs_data(db.Model):
    Id= Column(db.Integer, primary_key = True ,autoincrement = True)
    BlockName= Column(db.String, nullable= False)
    Contactor=Column(db.String, nullable= False)
    PhoneNo= Column(db.Integer, nullable=False)
    Scheme= Column(db.String, nullable=False)
    Place= Column(db.String, nullable=False)
    NameOfWork= Column(db.String, nullable= False)
    Material= Column(db.String, nullable=False)
    Quantity= Column(db.Integer, nullable=False)
    Author= Column(db.String, nullable= False)
    DateTime= Column(db.DateTime, default= datetime.utcnow)
    def __repr__(self):
        return "Id %r " % self.Id
    
class returns_data(db.Model):
    Id= Column(db.Integer, primary_key = True ,autoincrement = True)
    BlockName= Column(db.String, nullable= False)
    Contactor=Column(db.String, nullable= False)
    PhoneNo= Column(db.Integer, nullable=False)
    Scheme= Column(db.String, nullable=False)
    Place= Column(db.String, nullable=False)
    NameOfWork= Column(db.String, nullable= False)
    Material= Column(db.String, nullable=False)
    Quantity= Column(db.Integer, nullable=False)
    Author= Column(db.String, nullable= False)
    DateTime= Column(db.DateTime, default= datetime.utcnow)
    def __repr__(self):
        return "Id %r " % self.Id

class restock_data (db.Model):
    Id=Column(db.Integer, primary_key= True, autoincrement = True)
    BlockName= Column(db.String, nullable= False)
    SupplierName=Column(db.String, nullable= False)
    InvoiceNo= Column(db.Integer, nullable=False)
    VehicleNo= Column(db.Integer, nullable=False)
    Scheme= Column(db.String, nullable=False)
    Material= Column(db.String, nullable=False)
    Quantity= Column(db.Integer, nullable=False)
    Author= Column(db.String, nullable= False)
    DateTime= Column(db.DateTime, default= datetime.utcnow)
    def __repr__(self):
        return "Id %r " % self.Id

class transfer_data (db.Model):
    Id=Column(db.Integer, primary_key= True,autoincrement = True)
    BlockName= Column(db.String, nullable= False)
    FromScheme= Column(db.String, nullable=False)
    ToScheme= Column(db.String, nullable=False)
    Material= Column(db.String, nullable=False)
    Quantity= Column(db.Integer, nullable=False)
    Author= Column(db.String, nullable= False)
    DateTime= Column(db.DateTime, default= datetime.utcnow)
    def __repr__(self):
        return "Id %r " % self.Id

class cement_data (db.Model):
    Id=Column(db.Integer, primary_key= True,autoincrement = True)
    Scheme= Column(db.String, nullable= False)
    BlockName= Column(db.String, nullable= False, default=0)
    Cement=Column(db.Integer,  default=0)
    DateTime=Column(db.DateTime, default= datetime.utcnow)
    def __repr__(self):
        return "Id %r " % self.Id

class steel_data (db.Model):
    Id=Column(db.Integer, primary_key= True,autoincrement = True)
    Scheme= Column(db.String, nullable= False)
    BlockName= Column(db.String, nullable= False, default=0)
    Steel_8mm=Column(db.Integer,  default=0)
    Steel_10mm=Column(db.Integer,  default=0)
    Steel_12mm=Column(db.Integer,  default=0)
    Steel_16mm=Column(db.Integer,  default=0)
    Steel_20mm=Column(db.Integer,  default=0)
    DateTime=Column(db.DateTime, default= datetime.utcnow)
    def __repr__(self):
        return "Id %r " % self.Id

class bitumen_data (db.Model):
    Id=Column(db.Integer, primary_key= True,autoincrement = True)
    Scheme= Column(db.String, nullable= False)
    BlockName= Column(db.String, nullable= False, default=0)
    Bitumen=Column(db.Integer,  default=0)
    Emulsion=Column(db.Integer,  default=0)
    DateTime=Column(db.DateTime, default= datetime.utcnow)
    def __repr__(self):
        return "Id %r " % self.Id

class other_data (db.Model):
    Id=Column(db.Integer, primary_key= True,autoincrement = True)
    Scheme= Column(db.String, nullable= False)
    BlockName= Column(db.String, nullable= False, default=0)
    Door=Column(db.Integer,  default=0)
    Window_1=Column(db.Integer,  default=0)
    Window_2=Column(db.Integer,  default=0)
    Toilet_Door=Column(db.Integer,  default=0)
    LogoTiles=Column(db.Integer,  default=0)
    DateTime=Column(db.DateTime, default= datetime.utcnow)
    def __repr__(self):
        return "Id %r " % self.Id

#Rendering 
######################################################################################
@app.route('/logs', methods =['POST','GET'])

def logs():
    if request.cookies.get('UserId'):
        accessid= request.cookies.get('AccessId')
        if request.method=='POST':
            accessid= request.cookies.get('AccessId')
            contactorname= request.form['contactor_name']
            phoneno= request.form['phno']
            scheme= request.form['scheme']
            place= request.form['place']
            nameofwork= request.form['name_of_work']
            material= request.form['material']
            quantity= request.form['quantity']
            blockname=request.cookies.get('BlockId')

            resp=make_response(redirect('/update_log'))
            resp.set_cookie('Name_update',contactorname)
            resp.set_cookie('Phno_update',phoneno )
            resp.set_cookie('Place_update',place )
            resp.set_cookie('Nameofwork_update',nameofwork)
            resp.set_cookie('Scheme_update',scheme )
            resp.set_cookie('Material_update',material)
            resp.set_cookie('Quantity_update',quantity)

            
            if material== 'cement':
                data= cement_data.query.filter(cement_data.BlockName.like(blockname)).filter(cement_data.Scheme.like(scheme)).first()
                
                if data:
                    if (int(data.Cement)-int(quantity)) >= 0:
                        data.Cement= int(data.Cement)- int(quantity)
                        try:
                            db.session.commit()
                            return resp
                        except:
                            return  render_template('logs.html',error='update_error', accessid=accessid)
                    else:
                        return render_template('logs.html',error='low_stock',material_name= material, scheme_name= scheme, accessid=accessid)
                else:
                    return render_template('logs.html',error='no_stock',material_name= material, scheme_name= scheme, accessid=accessid) 

            elif material== 'steel_8mm':
                data= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(scheme)).first()
                    
                if data:
                    if (int(data.Steel_8mm)-int(quantity)) >= 0:
                        data.Steel_8mm= int(data.Steel_8mm)- int(quantity)
                        try:
                            db.session.commit()                          
                            return resp
                        except:
                                return  render_template('logs.html',error='update_error', accessid=accessid) 
                        else:
                            return render_template('logs.html',error='low_stock',material_name= material, scheme_name= scheme, accessid=accessid)
                    else:
                        return render_template('logs.html',error='no_stock',material_name= material, scheme_name= scheme, accessid=accessid) 

            elif material== 'steel_10mm':
                data= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(scheme)).first()
                    
                if data:
                    if (int(data.Steel_10mm)-int(quantity)) >= 0:
                        data.Steel_10mm= int(data.Steel_10mm)- int(quantity)
                        try:
                            db.session.commit()                           
                            return resp
                        except:
                            return  render_template('logs.html',error='update_error', accessid=accessid)
                    else:
                        return render_template('logs.html',error='low_stock',material_name= material, scheme_name= scheme, accessid=accessid)
                else:
                    return render_template('logs.html',error='no_stock',material_name= material, scheme_name= scheme, accessid=accessid)  
            
            elif material== 'steel_12mm':
                data= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(scheme)).first()
                    
                if data:
                    if (int(data.Steel_12mm)-int(quantity)) >= 0:
                        data.Steel_12mm= int(data.Steel_12mm)- int(quantity)
                        try:
                            db.session.commit()
                            return resp
                        except:
                            return  render_template('logs.html',error='update_error', accessid=accessid) 
                    else:
                        return render_template('logs.html',error='low_stock',material_name= material, scheme_name= scheme, accessid=accessid)
                else:
                    return render_template('logs.html',error='no_stock',material_name= material, scheme_name= scheme, accessid=accessid) 
            elif material== 'steel_16mm':
                data= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(scheme)).first()
                    
                if data:
                    if (int(data.Steel_16mm)-int(quantity)) >= 0:
                        data.Steel_16mm= int(data.Steel_16mm)- int(quantity)
                        try:
                            db.session.commit()
                            return resp
                        except:
                            return  render_template('logs.html',error='update_error') 
                    else:
                        return render_template('logs.html',error='low_stock',material_name= material, scheme_name= scheme, accessid=accessid)
                else:
                    return render_template('logs.html',error='no_stock',material_name= material, scheme_name= scheme, accessid=accessid) 

            elif material== 'steel_20mm':
                data= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(scheme)).first()
                    
                if data:
                    if (int(data.Steel_20mm)-int(quantity)) >= 0:
                        data.Steel_20mm= int(data.Steel_20mm)- int(quantity)
                        try:
                            db.session.commit()
                            return resp
                        except:
                            return  render_template('logs.html',error='update_error', accessid=accessid)  
                    else:
                        return render_template('logs.html',error='low_stock',material_name= material, scheme_name= scheme, accessid=accessid)
                else:
                    return render_template('logs.html',error='no_stock',material_name= material, scheme_name= scheme, accessid=accessid) 

            elif material== 'bitumen':
                data= bitumen_data.query.filter(bitumen_data.BlockName.like(blockname)).filter(bitumen_data.Scheme.like(scheme)).first()
                    
                if data:
                    if (int(data.Bitumen)-int(quantity)) >= 0:
                        data.Bitumen= int(data.Bitumen)- int(quantity)
                        try:
                            db.session.commit()
                            return resp
                        except:
                            return  render_template('logs.html',error='update_error', accessid=accessid)  
                    else:
                        return render_template('logs.html',error='low_stock',material_name= material, scheme_name= scheme, accessid=accessid)
                else:
                    return render_template('logs.html',error='no_stock',material_name= material, scheme_name= scheme, accessid=accessid) 

            elif material== 'emulsion':
                data= bitumen_data.query.filter(bitumen_data.BlockName.like(blockname)).filter(bitumen_data.Scheme.like(scheme)).first()
                    
                if data:
                    if (int(data.Emulsion)-int(quantity)) >= 0:
                        data.Emulsion= int(data.Emulsion)- int(quantity)
                        try:
                            db.session.commit()
                            return resp
                        except:
                            return  render_template('logs.html',error='update_error', accessid=accessid)  
                    else:
                        return render_template('logs.html',error='low_stock',material_name= material, scheme_name= scheme, accessid=accessid)
                else:
                    return render_template('logs.html',error='no_stock',material_name= material, scheme_name= scheme, accessid=accessid) 

            elif material== 'window_1':
                data= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(scheme)).first()
                    
                if data:
                    if (int(data.Window_1)-int(quantity)) >= 0:
                        data.Window_1= int(data.Window_1)- int(quantity)
                        try:                            
                            db.session.commit()                            
                            return resp
                        except:
                            return  render_template('logs.html',error='update_error', accessid=accessid) 
                    else:
                        return render_template('logs.html',error='low_stock',material_name= material, scheme_name= scheme, accessid=accessid)
                else:
                    return render_template('logs.html',error='no_stock',material_name= material, scheme_name= scheme, accessid=accessid)   

            elif material== 'window_2':
                data= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(scheme)).first()
                    
                if data:
                    if (int(data.Window_2)-int(quantity)) >= 0:
                        data.Window_2= int(data.Window_2)- int(quantity)
                        try:                            
                            db.session.commit()            
                            return resp
                        except:
                            return  render_template('logs.html',error='update_error', accessid=accessid)  
                    else:
                        return render_template('logs.html',error='low_stock',material_name= material, scheme_name= scheme, accessid=accessid)
                else:
                    return render_template('logs.html',error='no_stock',material_name= material, scheme_name= scheme, accessid=accessid) 

            elif material== 'door':
                data= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(scheme)).first()
                    
                if data:
                    if (int(data.Door)-int(quantity)) >= 0:
                        data.Door= int(data.Door)- int(quantity)
                        try:                           
                            db.session.commit()    
                            return resp
                        except:
                            return  render_template('logs.html',error='update_error', accessid=accessid) 
                    else:
                        return render_template('logs.html',error='low_stock',material_name= material, scheme_name= scheme, accessid=accessid)
                else:
                    return render_template('logs.html',error='no_stock',material_name= material, scheme_name= scheme, accessid=accessid) 

            elif material== 'toilet_door':
                data= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(scheme)).first()
                    
                if data:
                    if (int(data.Toilet_Door)-int(quantity)) >= 0:
                        data.Toilet_Door= int(data.Toilet_Door)- int(quantity)
                        try:                     
                            db.session.commit()
                            return resp
                        except:
                            return  render_template('logs.html',error='update_error', accessid=accessid)
                    else:
                        return render_template('logs.html',error='low_stock',material_name= material, scheme_name= scheme, accessid=accessid)
                else:
                    return render_template('logs.html',error='no_stock',material_name= material, scheme_name= scheme, accessid=accessid) 
            else:
                data= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(scheme)).first()
                    
                if data:
                    if (int(data.LogoTiles)-int(quantity)) >= 0:
                        data.LogoTiles= int(data.LogoTiles)- int(quantity)
                        try:                          
                            db.session.commit()                            
                            return resp
                        except:
                            return  render_template('logs.html',error='update_error', accessid=accessid)  
                    else:
                        return render_template('logs.html',error='low_stock',material_name= material, scheme_name= scheme, accessid=accessid)
                else:
                    return render_template('logs.html',error='no_stock',material_name= material, scheme_name= scheme, accessid=accessid) 
        else:
            return render_template('logs.html', accessid=accessid)
    else:
        return redirect('/')
#######################################################################################################################################

@app.route('/update_log')

def update():
    if request.cookies.get('UserId'):
        accessid= request.cookies.get('AccessId')
        blockname=request.cookies.get('BlockId')
        author= request.cookies.get('UserId')
        contactorname=request.cookies.get('Name_update')
        phoneno=request.cookies.get('Phno_update')
        scheme=request.cookies.get('Scheme_update')
        place=request.cookies.get('Place_update')
        nameofwork=request.cookies.get('Nameofwork_update')
        quantity= request.cookies.get('Quantity_update')
        material = request.cookies.get('Material_update')
        
        new_log= logs_data( BlockName= blockname, Contactor = contactorname, PhoneNo= phoneno, Scheme= scheme, Place= place, NameOfWork= nameofwork, Material= material, Quantity= quantity,Author= author)
        db.session.add(new_log)
        db.session.commit()

        def reval(val):
            if val== None:
                return 0
            else:
                return int(val)

        cement=cement_data.query.with_entities(
                        func.sum(cement_data.Cement).label("sum")
                    ).filter(cement_data.BlockName.like(blockname)).scalar()

        cement= reval(cement)

        steel1=steel_data.query.with_entities(
                        func.sum(steel_data.Steel_8mm)
                    ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel1=reval(steel1)
                    
        steel2=steel_data.query.with_entities(
                        func.sum(steel_data.Steel_10mm)
                    ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel2=reval(steel2)

        steel3=steel_data.query.with_entities(
                        func.sum(steel_data.Steel_12mm)
                    ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel3=reval(steel3)

        steel4=steel_data.query.with_entities(
                        func.sum(steel_data.Steel_16mm)
                    ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel4=reval(steel4)

        steel5=steel_data.query.with_entities(
                        func.sum(steel_data.Steel_20mm)
                    ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel5=reval(steel5)

        steel= steel1+steel2+steel3+steel4+steel5

        bitumen=bitumen_data.query.with_entities(
                        func.sum(bitumen_data.Bitumen).label("sum")
                    ).filter(bitumen_data.BlockName.like(blockname)).scalar()

        bitumen= reval(bitumen)

        emulsion=bitumen_data.query.with_entities(
                        func.sum(bitumen_data.Emulsion).label("sum")
                    ).filter(bitumen_data.BlockName.like(blockname)).scalar()

        emulsion= reval(emulsion)

        door=other_data.query.with_entities(
                        func.sum(other_data.Door).label("sum")
                    ).filter(other_data.BlockName.like(blockname)).scalar()

        door= reval(door)

        toiletdoor=other_data.query.with_entities(
                        func.sum(other_data.Toilet_Door).label("sum")
                    ).filter(other_data.BlockName.like(blockname)).scalar()

        toiletdoor= reval(toiletdoor)

        window1=other_data.query.with_entities(
                        func.sum(other_data.Window_1).label("sum")
                    ).filter(other_data.BlockName.like(blockname)).scalar()

        window1= reval(window1)

        window2=other_data.query.with_entities(
                        func.sum(other_data.Window_2).label("sum")
                    ).filter(other_data.BlockName.like(blockname)).scalar()

        window2= reval(window2)

        logo=other_data.query.with_entities(
                        func.sum(other_data.LogoTiles).label("sum")
                    ).filter(other_data.BlockName.like(blockname)).scalar()

        logo= reval(logo)
                    
        other= door+ window1+ window2+ logo+ toiletdoor

        resp=make_response(render_template('home.html',state='log', accessid=accessid,cement=cement, steel= steel, bitumen=bitumen, emulsion=emulsion, other= other))

        resp.set_cookie('Name_update', '', expires=0)
        resp.set_cookie('Phno_update', '', expires=0)
        resp.set_cookie('Scheme_update', '', expires=0)
        resp.set_cookie('Place_update', '', expires=0)
        resp.set_cookie('Nameofwork_update', '', expires=0)
        resp.set_cookie('Quantity_update', '', expires=0)
        resp.set_cookie('Material_update', '', expires=0)
        return resp

##################################################################################################

@app.route('/restock', methods=['POST','GET'])

def restock():
    if request.cookies.get('UserId'):
        accessid= request.cookies.get('AccessId')
        if request.method== 'POST':
            accessid= request.cookies.get('AccessId')
            suppliername = request.form['supplier_name']
            invoiceno=  request.form['invoice_no']
            vehicleno=  request.form['vehicle_no']
            scheme= request.form['scheme']
            material=  request.form['material']
            quantity=  request.form['quantity']
            blockname=request.cookies.get('BlockId')
            
            resp=make_response(redirect('/update_restock'))
            resp.set_cookie('Name_update',suppliername)
            resp.set_cookie('Invoiceno_update',invoiceno )
            resp.set_cookie('Vehicleno_update',vehicleno )
            resp.set_cookie('Scheme_update',scheme )
            resp.set_cookie('Material_update',material)
            resp.set_cookie('Quantity_update',quantity)

            if material== 'cement':
                data= cement_data.query.filter(cement_data.BlockName.like(blockname)).filter(cement_data.Scheme.like(scheme)).first()
                if data:
                        data.Cement= int(data.Cement)+ int(quantity)
                        try:                            
                            db.session.commit()
                            return resp
                        except:
                            return render_template('restock.html',error='update_error', accessid=accessid) 
                else:
                    new_stock= cement_data(BlockName= blockname, Scheme=scheme, Cement= quantity)
                    try:
                        db.session.add(new_stock)
                        db.session.commit()                        
                        return resp
                    except:
                        return render_template('restock.html',error='create_error', accessid=accessid)

            elif material== 'steel_8mm':
                data= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(scheme)).first()
                
                if data:
                        data.Steel_8mm= int(data.Steel_8mm)+ int(quantity)
                        try:                            
                            db.session.commit()                            
                            return resp
                        except:
                            return render_template('restock.html',error='update_error', accessid=accessid)  
                else:
                    new_stock= steel_data(BlockName= blockname, Scheme=scheme, Steel_8mm= quantity)
                    try:
                        db.session.add(new_stock)
                        db.session.commit()                        
                        return resp
                    except:
                        return render_template('restock.html',error='create_error', accessid=accessid)  

            elif material== 'steel_10mm':
                data= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(scheme)).first()
                
                if data:
                        data.Steel_10mm= int(data.Steel_10mm)+ int(quantity)
                        try:                            
                            db.session.commit()                            
                            return resp
                        except:
                            return render_template('restock.html',error='update_error', accessid=accessid)  
                else:
                    new_stock= steel_data(BlockName= blockname, Scheme=scheme, Steel_10mm= quantity)
                    try:
                        db.session.add(new_stock)
                        db.session.commit()                        
                        return resp
                    except:
                        return render_template('restock.html',error='create_error', accessid=accessid)

            elif material== 'steel_12mm':
                data= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(scheme)).first()
                
                if data:
                        data.Steel_12mm= int(data.Steel_12mm)+ int(quantity)
                        try:                            
                            db.session.commit()
                            return resp
                        except:
                            return render_template('restock.html',error='update_error', accessid=accessid)  
                else:
                    new_stock= steel_data(BlockName= blockname, Scheme=scheme, Steel_12mm= quantity)
                    try:
                        db.session.add(new_stock)
                        db.session.commit()
                        return resp
                    except:
                        return render_template('restock.html',error='create_error', accessid=accessid) 

            elif material== 'steel_16mm':
                data= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(scheme)).first()
                
                if data:
                        data.Steel_16mm= int(data.Steel_16mm)+ int(quantity)
                        try: 
                            db.session.commit()                            
                            return resp
                        except:
                            return render_template('restock.html',error='update_error', accessid=accessid)  
                else:
                    new_stock= steel_data(BlockName= blockname, Scheme=scheme, Steel_16mm= quantity)
                    try:
                        db.session.add(new_stock)
                        db.session.commit()                        
                        return resp
                    except:
                        return render_template('restock.html',error='create_error', accessid=accessid)

            elif material== 'steel_20mm':
                data= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(scheme)).first()
                
                if data:
                        data.Steel_20mm= int(data.Steel_20mm)+ int(quantity)
                        try:                            
                            db.session.commit()                            
                            return resp
                        except:
                            return render_template('restock.html',error='update_error', accessid=accessid)  
                else:
                    new_stock= steel_data(BlockName= blockname, Scheme=scheme, Steel_20mm= quantity)
                    try:
                        db.session.add(new_stock)
                        db.session.commit()                        
                        return resp
                    except:
                        return render_template('restock.html',error='create_error', accessid=accessid)  

            elif material== 'bitumen':
                data= bitumen_data.query.filter(bitumen_data.BlockName.like(blockname)).filter(bitumen_data.Scheme.like(scheme)).first()
                
                if data:
                        data.Bitumen= int(data.Bitumen)+ int(quantity)
                        try:                            
                            db.session.commit()                            
                            return resp
                        except:
                            return render_template('restock.html',error='update_error', accessid=accessid)  
                else:
                    new_stock= bitumen_data(BlockName= blockname, Scheme=scheme, Bitumen= quantity)
                    try:
                        db.session.add(new_stock)
                        db.session.commit()                        
                        return resp
                    except:
                        return render_template('restock.html',error='create_error', accessid=accessid)  

            elif material== 'emulsion':
                data= bitumen_data.query.filter(bitumen_data.BlockName.like(blockname)).filter(bitumen_data.Scheme.like(scheme)).first()
                
                if data:
                        data.Emulsion= int(data.Emulsion)+ int(quantity)
                        try:                            
                            db.session.commit()                            
                            return resp
                        except:
                            return render_template('restock.html',error='update_error', accessid=accessid)  
                else:
                    new_stock= bitumen_data(BlockName= blockname, Scheme=scheme, Emulsion= quantity)
                    try:
                        db.session.add(new_stock)
                        db.session.commit()                        
                        return resp
                    except:
                        return render_template('restock.html',error='create_error', accessid=accessid)

            elif material== 'window_1':
                data= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(scheme)).first()
                
                if data:
                        data.Window_1= int(data.Window_1)+ int(quantity)
                        try:
                            db.session.commit()                            
                            return resp
                        except:
                            return render_template('restock.html',error='update_error', accessid=accessid)  
                else:
                    new_stock= other_data(BlockName= blockname, Scheme=scheme, Window_1 = quantity)
                    try:
                        db.session.add(new_stock)
                        db.session.commit()                        
                        return resp
                    except:
                        return render_template('restock.html',error='create_error', accessid=accessid)

            elif material== 'window_2':
                data= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(scheme)).first()
                
                if data:
                        data.Window_2= int(data.Window_2)+ int(quantity)
                        try:                            
                            db.session.commit()                            
                            return resp
                        except:
                           return render_template('restock.html',error='update_error', accessid=accessid)  
                else:
                    new_stock= other_data(BlockName= blockname, Scheme=scheme, Window_2 = quantity)
                    try:
                        db.session.add(new_stock)
                        db.session.commit()                        
                        return resp
                    except:
                        return render_template('restock.html',error='create_error', accessid=accessid)

            elif material== 'door':
                data= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(scheme)).first()
                
                if data:
                        data.Door= int(data.Door)+ int(quantity)
                        try:                            
                            db.session.commit()                          
                            return resp
                        except:
                            return render_template('restock.html',error='update_error', accessid=accessid) 
                else:
                    new_stock= other_data(BlockName= blockname, Scheme=scheme, Door= quantity)
                    try:
                        db.session.add(new_stock)
                        db.session.commit()                        
                        return resp
                    except:
                        return render_template('restock.html',error='create_error', accessid=accessid) 

            elif material== 'toilet_door':
                data= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(scheme)).first()
                
                if data:
                        data.Toilet_Door= int(data.Toilet_Door)+ int(quantity)
                        try:                            
                            db.session.commit()                            
                            return resp
                        except:
                           return render_template('restock.html',error='update_error', accessid=accessid)  
                else:
                    new_stock= other_data(BlockName= blockname, Scheme=scheme, Toilet_Door= quantity)
                    try:
                        db.session.add(new_stock)
                        db.session.commit()                        
                        return resp
                    except:
                        return render_template('restock.html',error='create_error', accessid=accessid)
            else:
                data= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(scheme)).first()
                
                if data:
                        data.LogoTiles= int(data.LogoTiles)+ int(quantity)
                        try:                            
                            db.session.commit()                            
                            return resp
                        except:
                           return render_template('restock.html',error='update_error', accessid=accessid)  
                else:
                    new_stock= other_data(BlockName= blockname, Scheme=scheme, LogoTiles= quantity)
                    try:
                        db.session.add(new_stock)
                        db.session.commit()                        
                        return resp
                    except:
                        return render_template('restock.html',error='create_error', accessid=accessid)      
        else:
            return render_template('restock.html', accessid=accessid)
    else:
        return redirect('/')

#######################################################################################################################################

@app.route('/update_restock')

def update_restock():
    if request.cookies.get('UserId'):
        accessid= request.cookies.get('AccessId')
        blockname= request.cookies.get('BlockId')
        scheme= request.cookies.get('Scheme_update')
        quantity= request.cookies.get('Quantity_update')
        material = request.cookies.get('Material_update')
        suppliername = request.cookies.get('Name_update')
        invoiceno= request.cookies.get('Invoiceno_update')
        vehicleno= request.cookies.get('Vehicleno_update')
        author= request.cookies.get('UserId')

        new_restock= restock_data( BlockName= blockname, SupplierName= suppliername, InvoiceNo= invoiceno, VehicleNo=vehicleno, Scheme=scheme, Material=material, Quantity=quantity, Author=author)
        db.session.add(new_restock)
        db.session.commit()

        def reval(val):
            if val== None:
                return 0
            else:
                return int(val)

        cement=cement_data.query.with_entities(
                        func.sum(cement_data.Cement).label("sum")
                    ).filter(cement_data.BlockName.like(blockname)).scalar()

        cement= reval(cement)

        steel1=steel_data.query.with_entities(
                        func.sum(steel_data.Steel_8mm)
                    ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel1=reval(steel1)
                    
        steel2=steel_data.query.with_entities(
                        func.sum(steel_data.Steel_10mm)
                    ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel2=reval(steel2)

        steel3=steel_data.query.with_entities(
                        func.sum(steel_data.Steel_12mm)
                    ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel3=reval(steel3)

        steel4=steel_data.query.with_entities(
                        func.sum(steel_data.Steel_16mm)
                    ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel4=reval(steel4)

        steel5=steel_data.query.with_entities(
                        func.sum(steel_data.Steel_20mm)
                    ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel5=reval(steel5)

        steel= steel1+steel2+steel3+steel4+steel5

        bitumen=bitumen_data.query.with_entities(
                        func.sum(bitumen_data.Bitumen).label("sum")
                    ).filter(bitumen_data.BlockName.like(blockname)).scalar()

        bitumen= reval(bitumen)

        emulsion=bitumen_data.query.with_entities(
                        func.sum(bitumen_data.Emulsion).label("sum")
                    ).filter(bitumen_data.BlockName.like(blockname)).scalar()

        emulsion= reval(emulsion)

        door=other_data.query.with_entities(
                        func.sum(other_data.Door).label("sum")
                    ).filter(other_data.BlockName.like(blockname)).scalar()

        door= reval(door)

        toiletdoor=other_data.query.with_entities(
                        func.sum(other_data.Toilet_Door).label("sum")
                    ).filter(other_data.BlockName.like(blockname)).scalar()

        toiletdoor= reval(toiletdoor)

        window1=other_data.query.with_entities(
                        func.sum(other_data.Window_1).label("sum")
                    ).filter(other_data.BlockName.like(blockname)).scalar()

        window1= reval(window1)

        window2=other_data.query.with_entities(
                        func.sum(other_data.Window_2).label("sum")
                    ).filter(other_data.BlockName.like(blockname)).scalar()

        window2= reval(window2)

        logo=other_data.query.with_entities(
                        func.sum(other_data.LogoTiles).label("sum")
                    ).filter(other_data.BlockName.like(blockname)).scalar()

        logo= reval(logo)
                    
        other= door+ window1+ window2+ logo+ toiletdoor

        resp=make_response(render_template('home.html',state='restock', accessid=accessid,cement=cement, steel= steel, bitumen=bitumen, emulsion=emulsion, other= other))
        
        resp.set_cookie('Name_update', '', expires=0)
        resp.set_cookie('Invoiceno_update', '', expires=0)
        resp.set_cookie('Scheme_update', '', expires=0)
        resp.set_cookie('Vehicleno_update', '', expires=0)
        resp.set_cookie('Quantity_update', '', expires=0)
        resp.set_cookie('Material_update', '', expires=0)
        return resp
    else:
        return redirect('/')

###############################################################################

@app.route('/returns', methods=['POST', 'GET'])

def returns():
    if request.cookies.get('UserId'):
        accessid= request.cookies.get('AccessId')
        if request.method=='POST':
            accessid= request.cookies.get('AccessId')
            contactorname= request.form['contactor_name']
            phoneno= request.form['phno']
            scheme= request.form['scheme']
            place= request.form['place']
            nameofwork= request.form['name_of_work']
            material= request.form['material']
            quantity= request.form['quantity']
            blockname=request.cookies.get('BlockId')

            resp=make_response(redirect('/update_returns'))
            resp.set_cookie('Name_update',contactorname)
            resp.set_cookie('Phno_update',phoneno )
            resp.set_cookie('Place_update',place )
            resp.set_cookie('Nameofwork_update',nameofwork)
            resp.set_cookie('Scheme_update',scheme )
            resp.set_cookie('Material_update',material)
            resp.set_cookie('Quantity_update',quantity)
            
            if material== 'cement':
                data= cement_data.query.filter(cement_data.BlockName.like(blockname)).filter(cement_data.Scheme.like(scheme)).first()
                
                if data:                    
                    data.Cement= int(data.Cement)+ int(quantity)
                    try:                            
                        db.session.commit()                        
                        return resp
                    except:
                        return render_template('returns.html',error='update_error', accessid=accessid)      
                else:
                    return render_template('returns.html',error='no_stock', scheme_name= scheme, accessid=accessid) 
            
            elif material== 'steel_8mm':
                data= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(scheme)).first()                
                
                if data:                    
                        data.Steel_8mm= int(data.Steel_8mm)+int(quantity)
                        try:                            
                            db.session.commit()                            
                            return resp
                        except:
                            return render_template('returns.html',error='update_error', accessid=accessid)      
                else:
                    return render_template('returns.html',error='no_stock', scheme_name= scheme, accessid=accessid)  

            elif material== 'steel_10mm':
                data= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(scheme)).first()
                
                if data:                    
                        data.Steel_10mm= int(data.Steel_10mm)+int(quantity)
                        try:                            
                            db.session.commit()                            
                            return resp
                        except:
                            return render_template('returns.html',error='update_error', accessid=accessid)      
                else:
                    return render_template('returns.html',error='no_stock', scheme_name= scheme, accessid=accessid) 

            elif material== 'steel_12mm':
                data= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(scheme)).first()
                
                if data:                    
                        data.Steel_12mm= int(data.Steel_12mm)+int(quantity)
                        try:                            
                            db.session.commit()                            
                            return resp
                        except:
                            return render_template('returns.html',error='update_error', accessid=accessid)      
                else:
                    return render_template('returns.html',error='no_stock', scheme_name= scheme, accessid=accessid) 

            elif material== 'steel_16mm':
                data= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(scheme)).first()
                
                if data:                    
                        data.Steel_16mm= int(data.Steel_16mm)+int(quantity)
                        try:                            
                            db.session.commit()                            
                            return resp
                        except:
                            return render_template('returns.html',error='update_error', accessid=accessid)      
                else:
                    return render_template('returns.html',error='no_stock', scheme_name= scheme, accessid=accessid) 

            elif material== 'steel_20mm':
                data= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(scheme)).first()
                
                if data:                    
                        data.Steel_20mm= int(data.Steel_20mm)+int(quantity)
                        try:                            
                            db.session.commit()                            
                            return resp
                        except:
                            return render_template('returns.html',error='update_error', accessid=accessid)      
                else:
                    return render_template('returns.html',error='no_stock', scheme_name= scheme, accessid=accessid)  

            elif material== 'bitumen':
                data= bitumen_data.query.filter(bitumen_data.BlockName.like(blockname)).filter(bitumen_data.Scheme.like(scheme)).first()
                
                if data:
                    data.Bitumen= int(data.Bitumen)+ int(quantity)
                    try:                            
                        db.session.commit()                        
                        return resp
                    except:
                        return render_template('returns.html',error='update_error', accessid=accessid)      
                else:
                    return render_template('returns.html',error='no_stock', scheme_name= scheme, accessid=accessid) 

            elif material== 'emulsion':
                data= bitumen_data.query.filter(bitumen_data.BlockName.like(blockname)).filter(bitumen_data.Scheme.like(scheme)).first()
                
                if data:
                    data.Emulsion= int(data.Emulsion)+ int(quantity)
                    try:                            
                        db.session.commit()                        
                        return resp
                    except:
                        return render_template('returns.html',error='update_error', accessid=accessid)      
                else:
                    return render_template('returns.html',error='no_stock', scheme_name= scheme, accessid=accessid) 

            elif material== 'window_1':
                data= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(scheme)).first()
                
                if data:                    
                    data.Window_1= int(data.Window_1)+ int(quantity)
                    try:                            
                        db.session.commit()                        
                        return resp
                    except:
                        return render_template('returns.html',error='update_error', accessid=accessid)      
                else:
                    return render_template('returns.html',error='no_stock', scheme_name= scheme, accessid=accessid)   

            elif material== 'window_2':
                data= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(scheme)).first()
                
                if data:                    
                    data.Window_2= int(data.Window_2)+ int(quantity)
                    try:                            
                        db.session.commit()                        
                        return resp
                    except:
                        return render_template('returns.html',error='update_error', accessid=accessid)      
                else:
                    return render_template('returns.html',error='no_stock', scheme_name= scheme, accessid=accessid)  

            elif material== 'door':
                data= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(scheme)).first()
                
                if data:                    
                        data.Door= int(data.Door)+ int(quantity)
                        try:                            
                            db.session.commit()                            
                            return resp
                        except:
                            return render_template('returns.html',error='update_error', accessid=accessid)      
                else:
                    return render_template('returns.html',error='no_stock', scheme_name= scheme, accessid=accessid)   
            
            elif material== 'toilet_door':
                data= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(scheme)).first()
                
                if data:                    
                        data.Toilet_Door= int(data.Toilet_Door)+ int(quantity)
                        try:                            
                            db.session.commit()                            
                            return resp
                        except:
                            return render_template('returns.html',error='update_error', accessid=accessid)      
                else:
                    return render_template('returns.html',error='no_stock', scheme_name= scheme, accessid=accessid)  
            else:
                data= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(scheme)).first()
                
                if data:                    
                        data.LogoTiles= int(data.LogoTiles)+int(quantity)
                        try:                            
                            db.session.commit()                            
                            return resp
                        except:
                            return render_template('returns.html',error='update_error', accessid=accessid)      
                else:
                    return render_template('returns.html',error='no_stock', scheme_name= scheme, accessid=accessid)  
            
        else:
            return render_template('returns.html', accessid=accessid)
    else:
        
        return redirect('/')

###############################################################################
@app.route('/update_returns')

def update_returns():
    if request.cookies.get('UserId'):
        accessid= request.cookies.get('AccessId')
        blockname= request.cookies.get('BlockId')
        author= request.cookies.get('UserId')
        contactorname=request.cookies.get('Name_update')
        phoneno=request.cookies.get('Phno_update')
        scheme=request.cookies.get('Scheme_update')
        place=request.cookies.get('Place_update')
        nameofwork=request.cookies.get('Nameofwork_update')
        quantity= request.cookies.get('Quantity_update')
        material = request.cookies.get('Material_update')

        new_returns= returns_data(BlockName=blockname, Contactor = contactorname, PhoneNo= phoneno, Scheme= scheme, Place= place, NameOfWork= nameofwork, Material= material, Quantity= quantity, Author= author)
        db.session.add(new_returns)
        db.session.commit()

        def reval(val):
            if val== None:
                return 0
            else:
                return int(val)

        cement=cement_data.query.with_entities(
                        func.sum(cement_data.Cement).label("sum")
                    ).filter(cement_data.BlockName.like(blockname)).scalar()

        cement= reval(cement)

        steel1=steel_data.query.with_entities(
                        func.sum(steel_data.Steel_8mm)
                    ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel1=reval(steel1)
                    
        steel2=steel_data.query.with_entities(
                        func.sum(steel_data.Steel_10mm)
                    ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel2=reval(steel2)

        steel3=steel_data.query.with_entities(
                        func.sum(steel_data.Steel_12mm)
                    ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel3=reval(steel3)

        steel4=steel_data.query.with_entities(
                        func.sum(steel_data.Steel_16mm)
                    ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel4=reval(steel4)

        steel5=steel_data.query.with_entities(
                        func.sum(steel_data.Steel_20mm)
                    ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel5=reval(steel5)

        steel= steel1+steel2+steel3+steel4+steel5

        bitumen=bitumen_data.query.with_entities(
                        func.sum(bitumen_data.Bitumen).label("sum")
                    ).filter(bitumen_data.BlockName.like(blockname)).scalar()

        bitumen= reval(bitumen)

        emulsion=bitumen_data.query.with_entities(
                        func.sum(bitumen_data.Emulsion).label("sum")
                    ).filter(bitumen_data.BlockName.like(blockname)).scalar()

        emulsion= reval(emulsion)

        door=other_data.query.with_entities(
                        func.sum(other_data.Door).label("sum")
                    ).filter(other_data.BlockName.like(blockname)).scalar()

        door= reval(door)

        toiletdoor=other_data.query.with_entities(
                        func.sum(other_data.Toilet_Door).label("sum")
                    ).filter(other_data.BlockName.like(blockname)).scalar()

        toiletdoor= reval(toiletdoor)

        window1=other_data.query.with_entities(
                        func.sum(other_data.Window_1).label("sum")
                    ).filter(other_data.BlockName.like(blockname)).scalar()

        window1= reval(window1)

        window2=other_data.query.with_entities(
                        func.sum(other_data.Window_2).label("sum")
                    ).filter(other_data.BlockName.like(blockname)).scalar()

        window2= reval(window2)

        logo=other_data.query.with_entities(
                        func.sum(other_data.LogoTiles).label("sum")
                    ).filter(other_data.BlockName.like(blockname)).scalar()

        logo= reval(logo)
                    
        other= door+ window1+ window2+ logo+ toiletdoor
        resp=make_response(render_template('home.html',state='returns', accessid=accessid,cement=cement, steel= steel, bitumen=bitumen, emulsion=emulsion, other= other))

        resp.set_cookie('Name_update', '', expires=0)
        resp.set_cookie('Phno_update', '', expires=0)
        resp.set_cookie('Scheme_update', '', expires=0)
        resp.set_cookie('Place_update', '', expires=0)
        resp.set_cookie('Nameofwork_update', '', expires=0)
        resp.set_cookie('Quantity_update', '', expires=0)
        resp.set_cookie('Material_update', '', expires=0)
        return resp

    else:
        return redirect('/')

#################################################################################################################################

@app.route('/transfer', methods= ['POST', 'GET'])

def transfer():
    if request.cookies.get('UserId'):
        accessid= request.cookies.get('AccessId')
        if request.method=='POST':
            accessid= request.cookies.get('AccessId')
            blockname=request.cookies.get('BlockId')
            fromscheme= request.form['from_scheme']
            toscheme= request.form['to_scheme']
            material= request.form['material']
            quantity= request.form['Quantity']

            resp= make_response(redirect('/update_transfer'))
            resp.set_cookie('ToScheme_update',toscheme)
            resp.set_cookie('FromScheme_update',fromscheme)
            resp.set_cookie('Material_update',material)
            resp.set_cookie('Quantity_update',quantity)
            
            if material== 'cement':
                
                todata= cement_data.query.filter(cement_data.BlockName.like(blockname)).filter(cement_data.Scheme.like(toscheme)).first()
                fromdata= cement_data.query.filter(cement_data.BlockName.like(blockname)).filter(cement_data.Scheme.like(fromscheme)).first()
                if fromdata:
                    if todata:
                        if (int(fromdata.Cement)-int( quantity)) >=0:
                            fromdata.Cement= int(fromdata.Cement) - int(quantity)
                            todata.Cement= int(todata.Cement)+ int(quantity)
                            try:
                                db.session.commit()
                                return resp
                            except:
                                return  render_template('transfer.html',error='update_error', accessid=accessid)  
                        else:
                            return render_template('transfer.html',error='low_stock', accessid=accessid ,material_name= material, scheme_name=fromscheme)
                    else:
                        if (int(fromdata.Cement)-int( quantity)) >=0:
                            fromdata.Cement= int(fromdata.Cement) - int(quantity)
                            to_data_update= cement_data(BlockName= blockname, Scheme=toscheme, Cement= quantity)
                            try:
                                db.session.add(to_data_update)
                                db.session.commit()
                                return resp
                            except:
                                return render_template('transfer.html',error='update_error', accessid=accessid)
                        else:  
                            return render_template('transfer.html',error='low_stock', accessid=accessid ,material_name= material, scheme_name=fromscheme)
                else:
                    return render_template('transfer.html',error='no_stock', accessid=accessid ,material_name= material, scheme_name= fromscheme)

            elif material== 'steel_8mm':
                todata= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(toscheme)).first()
                fromdata= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(fromscheme)).first()
                if fromdata:
                    if todata:
                        if (int(fromdata.Steel_8mm)-int( quantity)) >=0:
                            fromdata.Steel_8mm= int(fromdata.Steel_8mm) - int(quantity)
                            todata.Steel_8mm= int(todata.Steel_8mm)+ int(quantity)
                            try:
                                db.session.commit()
                                return resp
                            except:
                                return  render_template('transfer.html',error='update_error', accessid=accessid)  
                        else:
                            return render_template('transfer.html', accessid=accessid ,error='low_stock',material_name= material, scheme_name=fromscheme)
                    else:
                        if (int(fromdata.Steel_8mm)-int( quantity)) >=0:
                            fromdata.Steel_8mm= int(fromdata.Steel_8mm) - int(quantity)
                            to_data_update= steel_data(BlockName= blockname, Scheme=toscheme, Steel_8mm= quantity)
                            try:
                                db.session.add(to_data_update)
                                db.session.commit()                                
                                return resp
                            except:
                                return render_template('transfer.html',error='update_error', accessid=accessid)
                        else:  
                            return render_template('transfer.html', accessid=accessid ,error='low_stock',material_name= material, scheme_name=fromscheme)
                else:
                    return render_template('transfer.html',error='no_stock',material_name= material, scheme_name= fromscheme, accessid=accessid)

            elif material== 'steel_10mm':
                todata= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(toscheme)).first()
                fromdata= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(fromscheme)).first()
                if fromdata:
                    if todata:
                        if (int(fromdata.Steel_10mm)-int( quantity)) >=0:
                            fromdata.Steel_10mm= int(fromdata.Steel_10mm) - int(quantity)
                            todata.Steel_10mm= int(todata.Steel_10mm)+ int(quantity)
                            try:
                                db.session.commit()                                
                                return resp
                            except:
                                return  render_template('transfer.html',error='update_error', accessid=accessid)  
                        else:
                            return render_template('transfer.html',error='low_stock',material_name= material, scheme_name=fromscheme, accessid=accessid)
                    else:
                        if (int(fromdata.Steel_10mm)-int( quantity)) >=0:
                            fromdata.Steel_10mm= int(fromdata.Steel_10mm) - int(quantity)
                            to_data_update= steel_data(BlockName= blockname, Scheme=toscheme, Steel_10mm= quantity)
                            try:
                                db.session.add(to_data_update)
                                db.session.commit()                                
                                return resp
                            except:
                                return render_template('transfer.html',error='update_error', accessid=accessid)
                        else:  
                            return render_template('transfer.html',error='low_stock',material_name= material, scheme_name=fromscheme, accessid=accessid)
                else:
                    return render_template('transfer.html',error='no_stock',material_name= material, scheme_name= fromscheme, accessid=accessid)
            
            elif material== 'steel_12mm':
                todata= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(toscheme)).first()
                fromdata= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(fromscheme)).first()
                if fromdata:
                    if todata:
                        if (int(fromdata.Steel_12mm)-int( quantity)) >=0:
                            fromdata.Steel_12mm= int(fromdata.Steel_12mm) - int(quantity)
                            todata.Steel_12mm= int(todata.Steel_12mm)+ int(quantity)
                            try:
                                db.session.commit()                                
                                return resp
                            except:
                                return  render_template('transfer.html',error='update_error', accessid=accessid)  
                        else:
                            return render_template('transfer.html',error='low_stock',material_name= material, scheme_name=fromscheme, accessid=accessid)
                    else:
                        if (int(fromdata.Steel_12mm)-int( quantity)) >=0:
                            fromdata.Steel_12mm= int(fromdata.Steel_12mm) - int(quantity)
                            to_data_update= steel_data(BlockName= blockname, Scheme=toscheme, Steel_12mm= quantity)
                            try:
                                db.session.add(to_data_update)
                                db.session.commit()                                
                                return resp
                            except:
                                return render_template('transfer.html',error='update_error', accessid=accessid)
                        else:  
                            return render_template('transfer.html',error='low_stock',material_name= material, scheme_name=fromscheme, accessid=accessid)
                else:
                    return render_template('transfer.html',error='no_stock',material_name= material, scheme_name= fromscheme, accessid=accessid)
            
            elif material== 'steel_12mm':
                todata= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(toscheme)).first()
                fromdata= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(fromscheme)).first()
                if fromdata:
                    if todata:
                        if (int(fromdata.Steel_12mm)-int( quantity)) >=0:
                            fromdata.Steel_12mm= int(fromdata.Steel_12mm) - int(quantity)
                            todata.Steel_12mm= int(todata.Steel_12mm)+ int(quantity)
                            try:
                                db.session.commit()                                
                                return resp
                            except:
                                return  render_template('transfer.html',error='update_error', accessid=accessid)  
                        else:
                            return render_template('transfer.html',error='low_stock',material_name= material, scheme_name=fromscheme, accessid=accessid)
                    else:
                        if (int(fromdata.Steel_12mm)-int( quantity)) >=0:
                            fromdata.Steel_12mm= int(fromdata.Steel_12mm) - int(quantity)
                            to_data_update= steel_data(BlockName= blockname, Scheme=toscheme, Steel_12mm= quantity)
                            try:
                                db.session.add(to_data_update)
                                db.session.commit()                                
                                return resp
                            except:
                                return render_template('transfer.html',error='update_error', accessid=accessid)
                        else:  
                            return render_template('transfer.html',error='low_stock',material_name= material, scheme_name=fromscheme, accessid=accessid)
                else:
                    return render_template('transfer.html',error='no_stock',material_name= material, scheme_name= fromscheme, accessid=accessid)
            
            elif material== 'steel_16mm':
                todata= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(toscheme)).first()
                fromdata= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(fromscheme)).first()
                if fromdata:
                    if todata:
                        if (int(fromdata.Steel_16mm)-int( quantity)) >=0:
                            fromdata.Steel_16mm= int(fromdata.Steel_16mm) - int(quantity)
                            todata.Steel_16mm= int(todata.Steel_16mm)+ int(quantity)
                            try:
                                db.session.commit()                                
                                return resp
                            except:
                                return  render_template('transfer.html',error='update_error', accessid=accessid)  
                        else:
                            return render_template('transfer.html',error='low_stock',material_name= material, scheme_name=fromscheme, accessid=accessid)
                    else:
                        if (int(fromdata.Steel_16mm)-int( quantity)) >=0:
                            fromdata.Steel_16mm= int(fromdata.Steel_16mm) - int(quantity)
                            to_data_update= steel_data(BlockName= blockname, Scheme=toscheme, Steel_16mm= quantity)
                            try:
                                db.session.add(to_data_update)
                                db.session.commit()                                
                                return resp
                            except:
                                return render_template('transfer.html',error='update_error', accessid=accessid)
                        else:  
                            return render_template('transfer.html',error='low_stock',material_name= material, scheme_name=fromscheme, accessid=accessid)
                else:
                    return render_template('transfer.html',error='no_stock',material_name= material, scheme_name= fromscheme, accessid=accessid)

            elif material== 'steel_20mm':
                todata= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(toscheme)).first()
                fromdata= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(fromscheme)).first()
                if fromdata:
                    if todata:
                        if (int(fromdata.Steel_20mm)-int( quantity)) >=0:
                            fromdata.Steel_20mm= int(fromdata.Steel_20mm) - int(quantity)
                            todata.Steel_20mm= int(todata.Steel_20mm)+ int(quantity)
                            try:
                                db.session.commit()                                
                                return resp
                            except:
                                return  render_template('transfer.html',error='update_error', accessid=accessid)  
                        else:
                            return render_template('transfer.html',error='low_stock',material_name= material, scheme_name=fromscheme, accessid=accessid)
                    else:
                        if (int(fromdata.Steel_20mm)-int( quantity)) >=0:
                            fromdata.Steel_20mm= int(fromdata.Steel_20mm) - int(quantity)
                            to_data_update= steel_data(BlockName= blockname, Scheme=toscheme, Steel_20mm= quantity)
                            try:
                                db.session.add(to_data_update)
                                db.session.commit()                                
                                return resp
                            except:
                                return render_template('transfer.html',error='update_error', accessid=accessid)
                        else:  
                            return render_template('transfer.html',error='low_stock',material_name= material, scheme_name=fromscheme, accessid=accessid)
                else:
                    return render_template('transfer.html',error='no_stock',material_name= material, scheme_name= fromscheme, accessid=accessid)

            elif material== 'bitumen':
                todata= bitumen_data.query.filter(bitumen_data.BlockName.like(blockname)).filter(bitumen_data.Scheme.like(toscheme)).first()
                fromdata= bitumen_data.query.filter(bitumen_data.BlockName.like(blockname)).filter(bitumen_data.Scheme.like(fromscheme)).first()
                if fromdata:
                    if todata:
                        if (int(fromdata.Bitumen)-int( quantity)) >=0:
                            fromdata.Bitumen= int(fromdata.Bitumen) - int(quantity)
                            todata.Bitumen= int(todata.Bitumen)+ int(quantity)
                            try:
                                db.session.commit()                                
                                return resp
                            except:
                                return  render_template('transfer.html',error='update_error', accessid=accessid)  
                        else:
                            return render_template('transfer.html',error='low_stock',material_name= material, scheme_name=fromscheme, accessid=accessid)
                    else:
                        if (int(fromdata.Bitumen)-int( quantity)) >=0:
                            fromdata.Bitumen= int(fromdata.Bitumen) - int(quantity)
                            to_data_update= bitumen_data(BlockName= blockname, Scheme=toscheme, Bitumen= quantity)
                            try:
                                db.session.add(to_data_update)
                                db.session.commit()                                
                                return resp
                            except:
                                return render_template('transfer.html',error='update_error', accessid=accessid)
                        else:  
                            return render_template('transfer.html',error='low_stock',material_name= material, scheme_name=fromscheme, accessid=accessid)
                else:
                    return render_template('transfer.html',error='no_stock',material_name= material, scheme_name= fromscheme, accessid=accessid)

            elif material== 'emulsion':
                todata= bitumen_data.query.filter(bitumen_data.BlockName.like(blockname)).filter(bitumen_data.Scheme.like(toscheme)).first()
                fromdata= bitumen_data.query.filter(bitumen_data.BlockName.like(blockname)).filter(bitumen_data.Scheme.like(fromscheme)).first()
                if fromdata:
                    if todata:
                        if (int(fromdata.Emulsion)-int( quantity)) >=0:
                            fromdata.Emulsion= int(fromdata.Emulsion) - int(quantity)
                            todata.Emulsion= int(todata.Emulsion)+ int(quantity)
                            try:
                                db.session.commit()                                
                                return resp
                            except:
                                return  render_template('transfer.html',error='update_error', accessid=accessid)  
                        else:
                            return render_template('transfer.html',error='low_stock',material_name= material, scheme_name=fromscheme, accessid=accessid)
                    else:
                        if (int(fromdata.Emulsion)-int( quantity)) >=0:
                            fromdata.Emulsion= int(fromdata.Emulsion) - int(quantity)
                            to_data_update= bitumen_data(BlockName= blockname, Scheme=toscheme, Emulsion= quantity)
                            try:
                                db.session.add(to_data_update)
                                db.session.commit()                                
                                return resp
                            except:
                                return render_template('transfer.html',error='update_error', accessid=accessid)
                        else:  
                            return render_template('transfer.html',error='low_stock',material_name= material, scheme_name=fromscheme, accessid=accessid)
                else:
                    return render_template('transfer.html',error='no_stock',material_name= material, scheme_name= fromscheme, accessid=accessid)

            elif material== 'window_1':
                todata= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(toscheme)).first()
                fromdata= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(fromscheme)).first()
                if fromdata:
                    if todata:
                        if (int(fromdata.Window_1)-int( quantity)) >=0:
                            fromdata.Window_1= int(fromdata.Window_1) - int(quantity)
                            todata.Window_1= int(todata.Window_1)+ int(quantity)
                            try:
                                db.session.commit()
                                return resp
                            except:
                                return  render_template('transfer.html',error='update_error', accessid=accessid)  
                        else:
                            return render_template('transfer.html',error='low_stock',material_name= material, scheme_name=fromscheme, accessid=accessid)
                    else:
                        if (int(fromdata.Window_1)-int( quantity)) >=0:
                            fromdata.Window_1= int(fromdata.Window_1) - int(quantity)
                            to_data_update= other_data(BlockName= blockname, Scheme=toscheme, Window_1= quantity)
                            try:
                                db.session.add(to_data_update)
                                db.session.commit()                              
                                return resp
                            except:
                                return render_template('transfer.html',error='update_error', accessid=accessid)
                        else:  
                            return render_template('transfer.html',error='low_stock',material_name= material, scheme_name=fromscheme, accessid=accessid)
                else:
                    return render_template('transfer.html',error='no_stock',material_name= material, scheme_name= fromscheme, accessid=accessid)

            elif material== 'window_2':
                todata= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(toscheme)).first()
                fromdata= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(fromscheme)).first()
                if fromdata:
                    if todata:
                        if (int(fromdata.Window_2)-int( quantity)) >=0:
                            fromdata.Window_2= int(fromdata.Window_2) - int(quantity)
                            todata.Window_2= int(todata.Window_2)+ int(quantity)
                            try:
                                db.session.commit()                                
                                return resp
                            except:
                                return  render_template('transfer.html',error='update_error', accessid=accessid)  
                        else:
                            return render_template('transfer.html',error='low_stock',material_name= material, scheme_name=fromscheme, accessid=accessid)
                    else:
                        if (int(fromdata.Window_2)-int( quantity)) >=0:
                            fromdata.Window_2= int(fromdata.Window_2) - int(quantity)
                            to_data_update= other_data(BlockName= blockname, Scheme=toscheme, Window_2= quantity)
                            try:
                                db.session.add(to_data_update)
                                db.session.commit()                                
                                return resp
                            except:
                                return render_template('transfer.html',error='update_error', accessid=accessid)
                        else:  
                            return render_template('transfer.html',error='low_stock',material_name= material, scheme_name=fromscheme, accessid=accessid)
                else:
                    return render_template('transfer.html',error='no_stock',material_name= material, scheme_name= fromscheme, accessid=accessid)

            elif material== 'door':
                todata= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(toscheme)).first()
                fromdata= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(fromscheme)).first()
                if fromdata:
                    if todata:
                        if (int(fromdata.Door)-int( quantity)) >=0:
                            fromdata.Door= int(fromdata.Door) - int(quantity)
                            todata.Door= int(todata.Door)+ int(quantity)
                            try:
                                db.session.commit()                                
                                return resp
                            except:
                                return  render_template('transfer.html',error='update_error', accessid=accessid)  
                        else:
                            return render_template('transfer.html',error='low_stock',material_name= material, scheme_name=fromscheme, accessid=accessid)
                    else:
                        if (int(fromdata.Door)-int( quantity)) >=0:
                            fromdata.Door= int(fromdata.Door) - int(quantity)
                            to_data_update= other_data(BlockName= blockname, Scheme=toscheme, Door= quantity)
                            try:
                                db.session.add(to_data_update)
                                db.session.commit()                                
                                return resp
                            except:
                                return render_template('transfer.html',error='update_error', accessid=accessid)
                        else:  
                            return render_template('transfer.html',error='low_stock',material_name= material, scheme_name=fromscheme, accessid=accessid)
                else:
                    return render_template('transfer.html',error='no_stock',material_name= material, scheme_name= fromscheme, accessid=accessid)

            elif material== 'toilet_door':
                todata= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(toscheme)).first()
                fromdata= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(fromscheme)).first()
                if fromdata:
                    if todata:
                        if (int(fromdata.Toilet_Door)-int( quantity)) >=0:
                            fromdata.Toilet_Door= int(fromdata.Toilet_Door) - int(quantity)
                            todata.Toilet_Door= int(todata.Toilet_Door)+ int(quantity)
                            try:
                                db.session.commit()                                
                                return resp
                            except:
                                return  render_template('transfer.html',error='update_error', accessid=accessid)  
                        else:
                            return render_template('transfer.html',error='low_stock',material_name= material, scheme_name=fromscheme, accessid=accessid)
                    else:
                        if (int(fromdata.Toilet_Door)-int( quantity)) >=0:
                            fromdata.Toilet_Door= int(fromdata.Toilet_Door) - int(quantity)
                            to_data_update= other_data(BlockName= blockname, Scheme=toscheme, Toilet_Door= quantity)
                            try:
                                db.session.add(to_data_update)
                                db.session.commit()                                
                                return resp
                            except:
                                return render_template('transfer.html',error='update_error', accessid=accessid)
                        else:  
                            return render_template('transfer.html',error='low_stock',material_name= material, scheme_name=fromscheme, accessid=accessid)
                else:
                    return render_template('transfer.html',error='no_stock',material_name= material, scheme_name= fromscheme, accessid=accessid)
            else:
                todata= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(toscheme)).first()
                fromdata= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(fromscheme)).first()
                if fromdata:
                    if todata:
                        if (int(fromdata.LogoTiles)-int( quantity)) >=0:
                            fromdata.LogoTiles= int(fromdata.LogoTiles) - int(quantity)
                            todata.LogoTiles= int(todata.LogoTiles)+ int(quantity)
                            try:
                                db.session.commit()                                
                                return resp
                            except:
                                return  render_template('transfer.html',error='update_error', accessid=accessid)  
                        else:
                            return render_template('transfer.html',error='low_stock',material_name= material, scheme_name=fromscheme, accessid=accessid)
                    else:
                        if (int(fromdata.LogoTiles)-int( quantity)) >=0:
                            fromdata.LogoTiles= int(fromdata.LogoTiles) - int(quantity)
                            to_data_update= other_data(BlockName= blockname, Scheme=toscheme, LogoTiles= quantity)
                            try:
                                db.session.add(to_data_update)
                                db.session.commit()                                
                                return resp
                            except:
                                return render_template('transfer.html',error='update_error', accessid=accessid)
                        else:  
                            return render_template('transfer.html',error='low_stock',material_name= material, scheme_name=fromscheme, accessid=accessid)
                else:
                    return render_template('transfer.html',error='no_stock',material_name= material, scheme_name= fromscheme, accessid=accessid)    
        else:    
            return render_template('transfer.html', accessid=accessid)
    else:
        return redirect('/')

#######################################################################################################################################

@app.route('/update_transfer')

def update_transfer():
    if request.cookies.get('UserId'):
        accessid= request.cookies.get('AccessId')
        blockname= request.cookies.get('BlockId')
        toscheme= request.cookies.get('ToScheme_update')
        fromscheme= request.cookies.get('FromScheme_update')
        material= request.cookies.get('Material_update')
        quantity= request.cookies.get('Quantity_update')
        author= request.cookies.get('UserId')

        new_transfer= transfer_data( BlockName= blockname, FromScheme= fromscheme, ToScheme= toscheme, Material= material, Quantity= quantity, Author=author)
        db.session.add(new_transfer)
        db.session.commit()

        def reval(val):
            if val== None:
                return 0
            else:
                return int(val)

        cement=cement_data.query.with_entities(
                        func.sum(cement_data.Cement).label("sum")
                    ).filter(cement_data.BlockName.like(blockname)).scalar()

        cement= reval(cement)

        steel1=steel_data.query.with_entities(
                        func.sum(steel_data.Steel_8mm)
                    ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel1=reval(steel1)
                    
        steel2=steel_data.query.with_entities(
                        func.sum(steel_data.Steel_10mm)
                    ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel2=reval(steel2)

        steel3=steel_data.query.with_entities(
                        func.sum(steel_data.Steel_12mm)
                    ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel3=reval(steel3)

        steel4=steel_data.query.with_entities(
                        func.sum(steel_data.Steel_16mm)
                    ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel4=reval(steel4)

        steel5=steel_data.query.with_entities(
                        func.sum(steel_data.Steel_20mm)
                    ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel5=reval(steel5)

        steel= steel1+steel2+steel3+steel4+steel5

        bitumen=bitumen_data.query.with_entities(
                        func.sum(bitumen_data.Bitumen).label("sum")
                    ).filter(bitumen_data.BlockName.like(blockname)).scalar()

        bitumen= reval(bitumen)

        emulsion=bitumen_data.query.with_entities(
                        func.sum(bitumen_data.Emulsion).label("sum")
                    ).filter(bitumen_data.BlockName.like(blockname)).scalar()

        emulsion= reval(emulsion)

        door=other_data.query.with_entities(
                        func.sum(other_data.Door).label("sum")
                    ).filter(other_data.BlockName.like(blockname)).scalar()

        door= reval(door)

        toiletdoor=other_data.query.with_entities(
                        func.sum(other_data.Toilet_Door).label("sum")
                    ).filter(other_data.BlockName.like(blockname)).scalar()

        toiletdoor= reval(toiletdoor)

        window1=other_data.query.with_entities(
                        func.sum(other_data.Window_1).label("sum")
                    ).filter(other_data.BlockName.like(blockname)).scalar()

        window1= reval(window1)

        window2=other_data.query.with_entities(
                        func.sum(other_data.Window_2).label("sum")
                    ).filter(other_data.BlockName.like(blockname)).scalar()

        window2= reval(window2)

        logo=other_data.query.with_entities(
                        func.sum(other_data.LogoTiles).label("sum")
                    ).filter(other_data.BlockName.like(blockname)).scalar()

        logo= reval(logo)
                    
        other= door+ window1+ window2+ logo+ toiletdoor
        
        resp=make_response(render_template('home.html',state='transfer', accessid=accessid,cement=cement, steel= steel, bitumen=bitumen, emulsion=emulsion, other= other))
        
        resp.set_cookie('ToScheme_update', '', expires=0)
        resp.set_cookie('FromScheme_update', '', expires=0)
        resp.set_cookie('Quantity_update', '', expires=0)
        resp.set_cookie('Material_update', '', expires=0)
        
        return resp
    else:
        return redirect('/')

###############################################################################################

@app.route('/view_logs', methods=['POST','GET'])

def view_logs():
    if request.cookies.get('UserId'):
        blockname=request.cookies.get('BlockId')
        accessid= request.cookies.get('AccessId')
        logdata= logs_data.query.filter(cement_data.BlockName.like(blockname))
        
        return render_template('log_record.html', logdata=logdata, accessid=accessid)
    else:
       return redirect('/')

################################################################################################

@app.route('/view_transfer', methods=['POST','GET'])

def view_transfer():
    if request.cookies.get('UserId'):
        blockname=request.cookies.get('BlockId')
        accessid= request.cookies.get('AccessId')
        transferdata= transfer_data.query.filter(cement_data.BlockName.like(blockname))
        
        return render_template('transfer_record.html', transferdata= transferdata, accessid=accessid)
    else:
       return redirect('/')

#################################################################################################

@app.route('/view_restock', methods=['POST','GET'])
def view_restock():
    if request.cookies.get('UserId'):
        blockname=request.cookies.get('BlockId')
        accessid= request.cookies.get('AccessId')
        restockdata= restock_data.query.filter(restock_data.BlockName.like(blockname))
        
        return render_template('restock_record.html', restockdata= restockdata, accessid=accessid)
    else:
       return redirect('/')
#################################################################################################

@app.route('/view_return', methods=['POST','GET'])

def view_return():
    if request.cookies.get('UserId'):
        blockname=request.cookies.get('BlockId')
        accessid= request.cookies.get('AccessId')
        returndata= returns_data.query.filter(returns_data.BlockName.like(blockname))
        
        return render_template('return_record.html', returndata= returndata, accessid= accessid)
    else:
       return redirect('/')

#################################################################################################

@app.route('/view_cement', methods=['POST','GET'])

def view_cement():
    if request.cookies.get('UserId'):
        blockname=request.cookies.get('BlockId')
        accessid= request.cookies.get('AccessId')
        cementdata= cement_data.query.filter(cement_data.BlockName.like(blockname))
        def reval(val):
            if val== None:
                return 0
            else:
                return int(val)

        cement=cement_data.query.with_entities(
             func.sum(cement_data.Cement).label("sum")
         ).filter(cement_data.BlockName.like(blockname)).scalar()

        cement= reval(cement)
        return render_template('cement_record.html', cementdata= cementdata, cement= cement, accessid=accessid)
    else:
       return redirect('/')

#################################################################################################

@app.route('/view_steel', methods=['POST','GET'])
def view_steel():
    if request.cookies.get('UserId'):
        blockname=request.cookies.get('BlockId')
        accessid= request.cookies.get('AccessId')
        steeldata= steel_data.query.filter(steel_data.BlockName.like(blockname))

        def reval(val):
            if val== None:
                return 0
            else:
                return int(val)

        steel1=steel_data.query.with_entities(
             func.sum(steel_data.Steel_8mm)
         ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel1=reval(steel1)
         
        steel2=steel_data.query.with_entities(
             func.sum(steel_data.Steel_10mm)
         ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel2=reval(steel2)

        steel3=steel_data.query.with_entities(
             func.sum(steel_data.Steel_12mm)
         ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel3=reval(steel3)

        steel4=steel_data.query.with_entities(
             func.sum(steel_data.Steel_16mm)
         ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel4=reval(steel4)

        steel5=steel_data.query.with_entities(
             func.sum(steel_data.Steel_20mm)
         ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel5=reval(steel5)

        return render_template('steel_record.html', accessid=accessid, steeldata=steeldata, steel_8mm=steel1, steel_10mm= steel2, steel_12mm= steel3, steel_16mm=steel4, steel_20mm= steel5)
    else:
       return redirect('/')

#################################################################################################

@app.route('/view_bitumen', methods=['POST','GET'])

def view_bitumen():
    if request.cookies.get('UserId'):
        blockname=request.cookies.get('BlockId')
        accessid= request.cookies.get('AccessId')
        bitumendata= bitumen_data.query.filter(bitumen_data.BlockName.like(blockname))        

        def reval(val):
            if val== None:
                return 0
            else:
                return int(val)

        bitumen=bitumen_data.query.with_entities(
             func.sum(bitumen_data.Bitumen).label("sum")
         ).filter(bitumen_data.BlockName.like(blockname)).scalar()

        bitumen= reval(bitumen)

        emulsion=bitumen_data.query.with_entities(
             func.sum(bitumen_data.Emulsion).label("sum")
         ).filter(bitumen_data.BlockName.like(blockname)).scalar()

        emulsion= reval(emulsion)

        return render_template('bitumen_record.html', accessid=accessid, bitumendata=bitumendata, bitumen=bitumen, emulsion=emulsion)
    else:
       return redirect('/')
    
#################################################################################################

@app.route('/view_other', methods=['POST','GET'])

def view_other():
    if request.cookies.get('UserId'):
        blockname=request.cookies.get('BlockId')
        accessid= request.cookies.get('AccessId')
        otherdata= other_data.query.filter(other_data.BlockName.like(blockname))

        def reval(val):
            if val== None:
                return 0
            else:
                return int(val)

        door=other_data.query.with_entities(
             func.sum(other_data.Door).label("sum")
         ).filter(other_data.BlockName.like(blockname)).scalar()

        door= reval(door)

        toiletdoor=other_data.query.with_entities(
             func.sum(other_data.Toilet_Door).label("sum")
         ).filter(other_data.BlockName.like(blockname)).scalar()

        toiletdoor= reval(toiletdoor)

        window1=other_data.query.with_entities(
             func.sum(other_data.Window_1).label("sum")
         ).filter(other_data.BlockName.like(blockname)).scalar()

        window1= reval(window1)

        window2=other_data.query.with_entities(
             func.sum(other_data.Window_2).label("sum")
         ).filter(other_data.BlockName.like(blockname)).scalar()

        window2= reval(window2)

        logo=other_data.query.with_entities(
             func.sum(other_data.LogoTiles).label("sum")
         ).filter(other_data.BlockName.like(blockname)).scalar()

        logo= reval(logo)

        return render_template('other_record.html', accessid=accessid, otherdata=otherdata, door=door, window_1=window1, window_2= window2, logoTiles=logo, toilet_Door=toiletdoor)
    else:
       return redirect('/')

###################################################################################

@app.route('/home', methods=['POST','GET'])
def home():
    if request.cookies.get('UserId'):   
        blockname=request.cookies.get('BlockId')
        accessid= request.cookies.get('AccessId')

        def reval(val):
            if val== None:
                return 0
            else:
                return int(val)

        cement=cement_data.query.with_entities(
             func.sum(cement_data.Cement).label("sum")
         ).filter(cement_data.BlockName.like(blockname)).scalar()

        cement= reval(cement)

        steel1=steel_data.query.with_entities(
             func.sum(steel_data.Steel_8mm)
         ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel1=reval(steel1)
         
        steel2=steel_data.query.with_entities(
             func.sum(steel_data.Steel_10mm)
         ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel2=reval(steel2)

        steel3=steel_data.query.with_entities(
             func.sum(steel_data.Steel_12mm)
         ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel3=reval(steel3)

        steel4=steel_data.query.with_entities(
             func.sum(steel_data.Steel_16mm)
         ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel4=reval(steel4)

        steel5=steel_data.query.with_entities(
             func.sum(steel_data.Steel_20mm)
         ).filter(steel_data.BlockName.like(blockname)).scalar()

        steel5=reval(steel5)

        steel= steel1+steel2+steel3+steel4+steel5

        bitumen=bitumen_data.query.with_entities(
             func.sum(bitumen_data.Bitumen).label("sum")
         ).filter(bitumen_data.BlockName.like(blockname)).scalar()

        bitumen= reval(bitumen)

        emulsion=bitumen_data.query.with_entities(
             func.sum(bitumen_data.Emulsion).label("sum")
         ).filter(bitumen_data.BlockName.like(blockname)).scalar()

        emulsion= reval(emulsion)

        door=other_data.query.with_entities(
             func.sum(other_data.Door).label("sum")
         ).filter(other_data.BlockName.like(blockname)).scalar()

        door= reval(door)

        toiletdoor=other_data.query.with_entities(
             func.sum(other_data.Toilet_Door).label("sum")
         ).filter(other_data.BlockName.like(blockname)).scalar()

        toiletdoor= reval(toiletdoor)

        window1=other_data.query.with_entities(
             func.sum(other_data.Window_1).label("sum")
         ).filter(other_data.BlockName.like(blockname)).scalar()

        window1= reval(window1)

        window2=other_data.query.with_entities(
             func.sum(other_data.Window_2).label("sum")
         ).filter(other_data.BlockName.like(blockname)).scalar()

        window2= reval(window2)

        logo=other_data.query.with_entities(
             func.sum(other_data.LogoTiles).label("sum")
         ).filter(other_data.BlockName.like(blockname)).scalar()

        logo= reval(logo)
        
        other= door+ window1+ window2+ logo+ toiletdoor
        return render_template('home.html', accessid=accessid ,cement=cement, steel= steel, bitumen=bitumen, emulsion=emulsion, other= other)
    else:
       return redirect('/')

###################################################################################

@app.route('/edit', methods=["POST","GET"])
def edit():
    if request.cookies.get('UserId'):
        accessid= request.cookies.get('AccessId')
        if request.method== "POST":
            accessid= request.cookies.get('AccessId')
            contactorname= request.form['contactor_name']
            phoneno= request.form['phno']
            scheme= request.form['scheme']
            place= request.form['place']
            nameofwork= request.form['name_of_work']
            material= request.form['material']
            quantity= request.form['quantity']
            update_quantity= request.form['update_quantity']
            blockname=request.cookies.get('BlockId')
            
            data= logs_data.query.filter(logs_data.BlockName.like(blockname)).filter(logs_data.Contactor.like(contactorname)).filter(logs_data.Scheme.like(
                scheme)).filter(logs_data.Place.like(place)).filter(logs_data.NameOfWork.like(nameofwork)).filter(logs_data.Material.like(material)).filter(
                logs_data.Quantity.like(quantity)).first()
            

            if data:
                resp=make_response(redirect('/edit_update'))
                resp.set_cookie('Name_update',contactorname)
                resp.set_cookie('Phno_update',phoneno )
                resp.set_cookie('Place_update',place )
                resp.set_cookie('Nameofwork_update',nameofwork)
                resp.set_cookie('Scheme_update',scheme )
                resp.set_cookie('Material_update',material)
                resp.set_cookie('Quantity_update',quantity)
                resp.set_cookie('NewQuantity_update',update_quantity)

                if material == 'cement':
                    log= cement_data.query.filter(cement_data.BlockName.like(blockname)).filter(cement_data.Scheme.like(scheme)).first()
                    if log:
                        log.Cement= log.Cement + int(quantity)
                        log.Cement = log.Cement - int(update_quantity)

                        db.session.commit()
                        
                        return resp
                    else:
                        resp= render_template('edit.html', accessid=accessid, state= "no_stock", material_name= material, schem_name= scheme)
                        return resp

                elif material =='steel_8mm' or material=='steel_10mm' or material== 'steel_12mm' or material=='steel_16mm' or material=='steel_20mm':
                    log= steel_data.query.filter(steel_data.BlockName.like(blockname)).filter(steel_data.Scheme.like(scheme))

                    if log:
                        if material== 'steel_8mm':
                            log.Steel_8mm= log.Steel_8mm + quantity
                            log.Steel_8mm= log.Steel_8mm - update_quantity

                            db.session.commit()
                            return resp

                        elif material== 'steel_10mm':
                            log.Steel_10mm= log.Steel_10mm + quantity
                            log.Steel_10mm= log.Steel_10mm - update_quantity

                            db.session.commit()
                            return resp
                        
                        elif material== 'steel_12mm':
                            log.Steel_12mm= log.Steel_12mm + quantity
                            log.Steel_12mm= log.Steel_12mm - update_quantity

                            db.session.commit()
                            return resp
                        
                        elif material== 'steel_16mm':
                            log.Steel_16mm= log.Steel_16mm + quantity
                            log.Steel_16mm= log.Steel_16mm - update_quantity

                            db.session.commit()
                            return resp

                        elif material== 'steel_20mm':
                            log.Steel_20mm= log.Steel_20mm + quantity
                            log.Steel_20mm= log.Steel_20mm - update_quantity

                            db.session.commit()
                            return resp

                    else:
                        resp= render_template('edit.html', accessid=accessid, state= "no_stock", material_name= material, schem_name= scheme)
                        return resp 

                elif material=='bitumen' or 'emulsion':
                    log= bitumen_data.query.filter(bitumen_data.BlockName.like(blockname)).filter(bitumen_data.Scheme.like(scheme))
                    if log:
                        if material =='bitumen':
                            log.Bitumen = log.Bitumen + quantity
                            log.Bitumen = log.Bitumen - update_quantity

                            db.session.commit()
                            return resp 
                        
                        else:
                            log.Emulsion = log.Emulsion + quantity
                            log.Emulsion = log.Emulsion - update_quantity

                            db.session.commit()
                            return resp
                    else:
                        resp= render_template('edit.html', accessid=accessid, state= "no_stock", material_name= material, schem_name= scheme)
                        return resp
                else:
                    log= other_data.query.filter(other_data.BlockName.like(blockname)).filter(other_data.Scheme.like(scheme))

                    if log:
                        if material== 'door':
                            log.Door = log.Door+ quantity
                            log.Door = log.Door - update_quantity

                            db.session.commit()
                            return resp

                        elif material== 'door':
                            log.Door = log.Door+ quantity
                            log.Door = log.Door - update_quantity

                            db.session.commit()
                            return resp
                        
                        elif material== 'toilet_door':
                            log.Toilet_Door = log.Toilet_Door+ quantity
                            log.Toilet_Door = log.Toilet_Door - update_quantity

                            db.session.commit()
                            return resp

                        elif material== 'window_1':
                            log.Window_1 = log.Window_1+ quantity
                            log.Window_1 = log.Window_1 - update_quantity

                            db.session.commit()
                            return resp

                        elif material== 'window_2':
                            log.Window_2 = log.Window_2+ quantity
                            log.Window_2 = log.Window_2 - update_quantity

                            db.session.commit()
                            return resp
                        
                        else:
                            log.LogoTiles = log.LogoTiles+ quantity
                            log.LogoTiles = log.LogoTiles - update_quantity

                            db.session.commit()
                            return resp
                    else:
                        resp= render_template('edit.html', accessid=accessid, state= "no_stock", material_name= material, schem_name= scheme)
                        return resp
            else:
                resp= render_template('edit.html', accessid=accessid, state= "no_stock", material_name= material, schem_name= scheme)
                return resp
        else:
            return render_template('edit.html', accessid=accessid)
    else:
        return redirect('/')

##################################################################################
@app.route('/edit_update')
def edit_update():
    accessid= request.cookies.get('AccessId')
    blockname=request.cookies.get('BlockId')
    author= request.cookies.get('UserId')
    contactorname=request.cookies.get('Name_update')
    phoneno=request.cookies.get('Phno_update')
    scheme=request.cookies.get('Scheme_update')
    place=request.cookies.get('Place_update')
    nameofwork=request.cookies.get('Nameofwork_update')
    quantity= request.cookies.get('Quantity_update')
    update_quantity= request.cookies.get('NewQuantity_update')
    material = request.cookies.get('Material_update')
    def reval(val):
        if val== None:
            return 0
        else:
            return int(val)

    cement=cement_data.query.with_entities(
                    func.sum(cement_data.Cement).label("sum")
                ).filter(cement_data.BlockName.like(blockname)).scalar()

    cement= reval(cement)

    steel1=steel_data.query.with_entities(
                    func.sum(steel_data.Steel_8mm)
                ).filter(steel_data.BlockName.like(blockname)).scalar()

    steel1=reval(steel1)
                
    steel2=steel_data.query.with_entities(
                    func.sum(steel_data.Steel_10mm)
                ).filter(steel_data.BlockName.like(blockname)).scalar()

    steel2=reval(steel2)

    steel3=steel_data.query.with_entities(
                    func.sum(steel_data.Steel_12mm)
                ).filter(steel_data.BlockName.like(blockname)).scalar()

    steel3=reval(steel3)

    steel4=steel_data.query.with_entities(
                    func.sum(steel_data.Steel_16mm)
                ).filter(steel_data.BlockName.like(blockname)).scalar()

    steel4=reval(steel4)

    steel5=steel_data.query.with_entities(
                    func.sum(steel_data.Steel_20mm)
                ).filter(steel_data.BlockName.like(blockname)).scalar()

    steel5=reval(steel5)

    steel= steel1+steel2+steel3+steel4+steel5

    bitumen=bitumen_data.query.with_entities(
                    func.sum(bitumen_data.Bitumen).label("sum")
                ).filter(bitumen_data.BlockName.like(blockname)).scalar()

    bitumen= reval(bitumen)

    emulsion=bitumen_data.query.with_entities(
                    func.sum(bitumen_data.Emulsion).label("sum")
                ).filter(bitumen_data.BlockName.like(blockname)).scalar()

    emulsion= reval(emulsion)

    door=other_data.query.with_entities(
                    func.sum(other_data.Door).label("sum")
                ).filter(other_data.BlockName.like(blockname)).scalar()

    door= reval(door)

    toiletdoor=other_data.query.with_entities(
                    func.sum(other_data.Toilet_Door).label("sum")
                ).filter(other_data.BlockName.like(blockname)).scalar()

    toiletdoor= reval(toiletdoor)

    window1=other_data.query.with_entities(
                    func.sum(other_data.Window_1).label("sum")
                ).filter(other_data.BlockName.like(blockname)).scalar()

    window1= reval(window1)

    window2=other_data.query.with_entities(
                    func.sum(other_data.Window_2).label("sum")
                ).filter(other_data.BlockName.like(blockname)).scalar()

    window2= reval(window2)

    logo=other_data.query.with_entities(
                    func.sum(other_data.LogoTiles).label("sum")
                ).filter(other_data.BlockName.like(blockname)).scalar()

    logo= reval(logo)
                
    other= door+ window1+ window2+ logo+ toiletdoor 

    data= logs_data.query.filter(logs_data.BlockName.like(blockname)).filter(logs_data.Contactor.like(contactorname)).filter(logs_data.Scheme.like(
                scheme)).filter(logs_data.Place.like(place)).filter(logs_data.NameOfWork.like(nameofwork)).filter(logs_data.Material.like(material)).filter(
                logs_data.Quantity.like(quantity)).first()        
    

    data.Quantity= int(update_quantity)
    
    resp=make_response(render_template('home.html', accessid=accessid, state="edit",cement=cement, steel= steel, bitumen=bitumen, emulsion=emulsion, other= other))
    resp.set_cookie('Name_update', '', expires=0)
    resp.set_cookie('Phno_update', '', expires=0)
    resp.set_cookie('Scheme_update', '', expires=0)
    resp.set_cookie('Place_update', '', expires=0)
    resp.set_cookie('Nameofwork_update', '', expires=0)
    resp.set_cookie('Quantity_update', '', expires=0)
    resp.set_cookie('NewQuantity_update', '', expires=0)
    resp.set_cookie('Material_update', '', expires=0)

    db.session.commit()
    return resp

###################################################################################
@app.route('/', methods=['POST','GET'])
def login():
    
    if request.method=='POST':
        username= request.form['username']
        password= request.form['passwd']
        user = logins_data.query.filter_by(Username=username).first()
        if user :
            if user.Password == password:
                resp=make_response(redirect('/home'))
                resp.set_cookie('UserId',username)
                resp.set_cookie('BlockId',user.BlockName) 
                resp.set_cookie('AccessId',user.AccessType)
                return resp
            else :
                result= 'none'
                return render_template('login.html', result=result)
        else:
            result= 'none'
            return render_template('login.html',result= result) 
    else:
        return render_template('login.html')
    
################################################################################################################

@app.route('/register',methods=['POST','GET'])
def register():
    if request.cookies.get('UserId'):
        accessid= request.cookies.get('AccessId')
        if request.method=='POST':
            accessid= request.cookies.get('AccessId')
            username= request.form['username']
            password= request.form['password']
            block_name= request.form['block_name']
            access_type= request.form['access_type']
            
            new_login=logins_data( Username= username, Password= password, BlockName= block_name, AccessType= access_type )

            try:
                db.session.add(new_login)
                db.session.commit()
                return redirect('/home')
            except:
                return"There was a server isssue"
        else:
            return render_template('register.html', accessid=accessid)
    else:
        return redirect('/')
################################################################################################################

@app.route('/passwd_update',methods=['POST','GET'])
def passwd():
    if request.cookies.get('UserId'):
        accessid= request.cookies.get('AccessId')
        if request.method=='POST':
            accessid= request.cookies.get('AccessId')
            username= request.cookies.get('UserId')
            blockname= request.cookies.get('BlockId')
            password= request.form['password']
            new_password= request.form['new_password']

            log= logins_data.query.filter(logins_data.Username.like(username)).filter(logins_data.Password.like(password)).filter(logins_data.AccessType.like(accessid)).filter(logins_data.BlockName.like(blockname)).first()
            def reval(val):
                if val== None:
                    return 0
                else:
                    return int(val)

            cement=cement_data.query.with_entities(
                            func.sum(cement_data.Cement).label("sum")
                        ).filter(cement_data.BlockName.like(blockname)).scalar()

            cement= reval(cement)

            steel1=steel_data.query.with_entities(
                            func.sum(steel_data.Steel_8mm)
                        ).filter(steel_data.BlockName.like(blockname)).scalar()

            steel1=reval(steel1)
                        
            steel2=steel_data.query.with_entities(
                            func.sum(steel_data.Steel_10mm)
                        ).filter(steel_data.BlockName.like(blockname)).scalar()

            steel2=reval(steel2)

            steel3=steel_data.query.with_entities(
                            func.sum(steel_data.Steel_12mm)
                        ).filter(steel_data.BlockName.like(blockname)).scalar()

            steel3=reval(steel3)

            steel4=steel_data.query.with_entities(
                            func.sum(steel_data.Steel_16mm)
                        ).filter(steel_data.BlockName.like(blockname)).scalar()

            steel4=reval(steel4)

            steel5=steel_data.query.with_entities(
                            func.sum(steel_data.Steel_20mm)
                        ).filter(steel_data.BlockName.like(blockname)).scalar()

            steel5=reval(steel5)

            steel= steel1+steel2+steel3+steel4+steel5

            bitumen=bitumen_data.query.with_entities(
                            func.sum(bitumen_data.Bitumen).label("sum")
                        ).filter(bitumen_data.BlockName.like(blockname)).scalar()

            bitumen= reval(bitumen)

            emulsion=bitumen_data.query.with_entities(
                            func.sum(bitumen_data.Emulsion).label("sum")
                        ).filter(bitumen_data.BlockName.like(blockname)).scalar()

            emulsion= reval(emulsion)

            door=other_data.query.with_entities(
                            func.sum(other_data.Door).label("sum")
                        ).filter(other_data.BlockName.like(blockname)).scalar()

            door= reval(door)

            toiletdoor=other_data.query.with_entities(
                            func.sum(other_data.Toilet_Door).label("sum")
                        ).filter(other_data.BlockName.like(blockname)).scalar()

            toiletdoor= reval(toiletdoor)

            window1=other_data.query.with_entities(
                            func.sum(other_data.Window_1).label("sum")
                        ).filter(other_data.BlockName.like(blockname)).scalar()

            window1= reval(window1)

            window2=other_data.query.with_entities(
                            func.sum(other_data.Window_2).label("sum")
                        ).filter(other_data.BlockName.like(blockname)).scalar()

            window2= reval(window2)

            logo=other_data.query.with_entities(
                            func.sum(other_data.LogoTiles).label("sum")
                        ).filter(other_data.BlockName.like(blockname)).scalar()

            logo= reval(logo)
                        
            other= door+ window1+ window2+ logo+ toiletdoor
            if log:
                log.Password = ''
                log.Password = new_password

                db.session.commit()            
                return render_template('home.html',accessid=accessid, state='passwd',cement=cement, steel= steel, bitumen=bitumen, emulsion=emulsion, other= other)
            
            else:
                return render_template('passwd_update.html',accessid=accessid, error="invalid")      
            
        else:
            return render_template('passwd_update.html', accessid=accessid)
    else:
        return redirect('/')
################################################################################################################

@app.route('/delete',methods=['POST','GET'])
def delete():
    if request.cookies.get('UserId'):
        accessid= request.cookies.get('AccessId')
        if request.method=='POST':
            accessid= request.cookies.get('AccessId')
            username= request.cookies.get('UserId')
            blockname= request.cookies.get('BlockId')
            username= request.form['username']
            access= request.form['access_type']
            log= logins_data.query.filter(logins_data.Username.like(username)).filter(logins_data.AccessType.like(access)).filter(logins_data.BlockName.like(blockname)).first()

            def reval(val):
                if val== None:
                    return 0
                else:
                    return int(val)

            cement=cement_data.query.with_entities(
                            func.sum(cement_data.Cement).label("sum")
                        ).filter(cement_data.BlockName.like(blockname)).scalar()

            cement= reval(cement)

            steel1=steel_data.query.with_entities(
                            func.sum(steel_data.Steel_8mm)
                        ).filter(steel_data.BlockName.like(blockname)).scalar()

            steel1=reval(steel1)
                        
            steel2=steel_data.query.with_entities(
                            func.sum(steel_data.Steel_10mm)
                        ).filter(steel_data.BlockName.like(blockname)).scalar()

            steel2=reval(steel2)

            steel3=steel_data.query.with_entities(
                            func.sum(steel_data.Steel_12mm)
                        ).filter(steel_data.BlockName.like(blockname)).scalar()

            steel3=reval(steel3)

            steel4=steel_data.query.with_entities(
                            func.sum(steel_data.Steel_16mm)
                        ).filter(steel_data.BlockName.like(blockname)).scalar()

            steel4=reval(steel4)

            steel5=steel_data.query.with_entities(
                            func.sum(steel_data.Steel_20mm)
                        ).filter(steel_data.BlockName.like(blockname)).scalar()

            steel5=reval(steel5)

            steel= steel1+steel2+steel3+steel4+steel5

            bitumen=bitumen_data.query.with_entities(
                            func.sum(bitumen_data.Bitumen).label("sum")
                        ).filter(bitumen_data.BlockName.like(blockname)).scalar()

            bitumen= reval(bitumen)

            emulsion=bitumen_data.query.with_entities(
                            func.sum(bitumen_data.Emulsion).label("sum")
                        ).filter(bitumen_data.BlockName.like(blockname)).scalar()

            emulsion= reval(emulsion)

            door=other_data.query.with_entities(
                            func.sum(other_data.Door).label("sum")
                        ).filter(other_data.BlockName.like(blockname)).scalar()

            door= reval(door)

            toiletdoor=other_data.query.with_entities(
                            func.sum(other_data.Toilet_Door).label("sum")
                        ).filter(other_data.BlockName.like(blockname)).scalar()

            toiletdoor= reval(toiletdoor)

            window1=other_data.query.with_entities(
                            func.sum(other_data.Window_1).label("sum")
                        ).filter(other_data.BlockName.like(blockname)).scalar()

            window1= reval(window1)

            window2=other_data.query.with_entities(
                            func.sum(other_data.Window_2).label("sum")
                        ).filter(other_data.BlockName.like(blockname)).scalar()

            window2= reval(window2)

            logo=other_data.query.with_entities(
                            func.sum(other_data.LogoTiles).label("sum")
                        ).filter(other_data.BlockName.like(blockname)).scalar()

            logo= reval(logo)
                        
            other= door+ window1+ window2+ logo+ toiletdoor
            if log:
                db.session.delete(log)    
                db.session.commit()        
                return render_template('home.html',accessid=accessid, state='delete',cement=cement, steel= steel, bitumen=bitumen, emulsion=emulsion, other= other)
            
            else:
                return render_template('delete.html',accessid=accessid, error="invalid")    
            
        else:
            return render_template('delete.html', accessid=accessid)
    else:
        return redirect('/')
##############################################################################
@app.route('/logout')
def logout():
    if request.cookies.get('UserId'):
        resp= make_response(redirect('/'))
        resp.set_cookie('UserId', '', expires=0)
        resp.set_cookie('BlockId', '', expires=0)
        resp.set_cookie('AccessId', '', expires=0)
        return resp
    else:
        return redirect('/')

#############################################################################################################
if __name__ =="__main__":
    result= True
    app.run(debug=False)
