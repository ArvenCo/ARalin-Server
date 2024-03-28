from libs import *
from src.models import Project, db

class ProjectController:
    def index():
        projects = Project.query.all()
        return render_template('index.html', projects=projects)

    def store():
        title  = request.form['title']
        description = request.form['description']
        images = request.files.getlist('images')
        video = request.files['video']
        
        project = Project(title=title, description=description)
        db.session.add(project)
        db.session.commit()
        db.session.refresh(project)
        
        
        image_upload_path = f"static/uploads/{project.id}/images"
        video_upload_path = f"static/uploads/{project.id}/video"
        print(image_upload_path)
        if not os.path.exists(image_upload_path):
        
            os.makedirs(image_upload_path)
            os.makedirs(video_upload_path)
        for image in images:
            print(image.filename)
            image.save(os.path.join(image_upload_path, image.filename))
        video.save(os.path.join(video_upload_path, video.filename))
    