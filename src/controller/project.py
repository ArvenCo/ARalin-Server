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
        video.save(os.path.join(video_upload_path, 'project.mp4'))
    
    def gerate_qr(data):
        image = requests.get(url=f'https://api.qrserver.com/v1/create-qr-code/?size=1000x1000&data={data}')
        return send_file(path_or_file=io.BytesIO(image.content), download_name=f'{data} - QR.png', as_attachment=True)
    

    def get_chunk(id, byte1=None, byte2=None):
        full_path = f'static/uploads/{id}/video/project.mp4'
        if not os.path.exists(full_path) : return "Video Not Found", 404
        file_size = os.stat(full_path).st_size
        start = 0
        
        if byte1 < file_size:
            start = byte1
        if byte2:
            length = byte2 + 1 - byte1
        else:
            length = file_size - start

        with open(full_path, 'rb') as f:
            f.seek(start)
            chunk = f.read(length)
        return chunk, start, length, file_size