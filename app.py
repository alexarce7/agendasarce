import web
# @
from web import form
db = web.database(dbn='mysql', db='hfrxtn74simz55uf', user='j9v57928h6ddo4ch', pw='l92u4xftus69g5tn', host='rtzsaka6vivj2zp1.cbetxkdyhwsb.us-east-1.rds.amazonaws.com')
render=web.template.render('templates')
urls = (
    
    '/index','index',
    '/nuevo', 'nuevo',
    '/editar/(.+)','editar',
    '/eliminar/(.+)','eliminar'
)



myformAgenda=form.Form(
    form.Textbox('Nombre'), 
    form.Textbox('Telefono'),
    form.Textbox('Email'),
    
)
class index:
    def GET(self):
        
        result=db.select('contactos')
        return render.index(result)
    def POST(self):           
        raise web.seeother("/nuevo")    
class nuevo:
    def GET(self):
        formNew=myformAgenda()
        return render.nuevo(formNew)
    def POST(self): 
        formNew = myformAgenda()
        if not formNew.validates(): 
            return render.nuevo(formNew)
        else:
            db.insert('contactos', nombre=formNew.d.Nombre, 
            telefono=formNew.d.Telefono, email=formNew.d.Email)
            result=db.select('contactos')
            raise web.seeother('/index')
            

class editar:
    def GET(self,id):
        formEdit=myformAgenda()
        
        
        result=db.select('contactos', where= "id=%s"%(id))
        
        for row in result:
            formEdit['Nombre'].value=row.nombre
            formEdit['Telefono'].value=row.telefono
            formEdit['Email'].value=row.email
            
        return render.editar(formEdit)        
    def POST(self,id):
        formEdit=myformAgenda()
        if not formEdit.validates(): 
            return render.editar(formEdit)
        else:
            db.update('contactos', where='id=%s'%(id), nombre=formEdit.d.Nombre,
             telefono=formEdit.d.Telefono, email=formEdit.d.Email)
            result=db.select('contactos')
            raise web.seeother('/index')
class eliminar:
    def GET(self,id):
        formEdit=myformAgenda()
        
        result=db.select('contactos', where='id=%s'%(id))
        
        for row in result:
            formEdit['Nombre'].value=row.nombre
            formEdit['Telefono'].value=row.telefono
            formEdit['Email'].value=row.email
            
        return render.eliminar(formEdit)        
    def POST(self,id):
        formEdit=myformAgenda()
        if not formEdit.validates(): 
            return render.eliminar(formEdit)
        else:
            db.delete('contactos', where="id=%s"%(id))
            raise web.seeother('/index')


if __name__ == "__main__":
    
    app = web.application(urls, globals())
    app.run()
