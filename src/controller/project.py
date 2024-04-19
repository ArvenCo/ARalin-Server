from libs import *
from src.models import Project, db

class ProjectController:
    def __init__(self):
        ...
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
    
    def show(id):
        project = Project.query.get(id)
        return render_template('edit.html', project=project, images=os.listdir(f'static/uploads/{id}/images'))
    
    def update(id):
        
        project = Project.query.get(id)
        project.title = request.form['title']
        project.description = request.form['description']
        images = request.files.getlist('images')
        video = request.files['video']
        if request.files.getlist('images')[0].filename != '':
            _save_images(f"static/uploads/{id}/images", images)
        if video.filename != '':
            _save_video(f"static/uploads/{id}/video", video)
        db.session.commit()
        return redirect(url_for('web.edit', id=id))

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
    
    def get_images(id):
        return os.listdir(f'static/uploads/{id}/images')
    
    def delete(id):
        Project.query.filter_by(id=id).delete()
        shutil.rmtree(f'static/uploads/{id}')
        return redirect(url_for('web.index'))
    
def _save_images( path, images):
    _clear_dir(path)
    if not os.path.exists(path):
        os.makedirs(path)
    for image in images:
        print(image.filename)
        image.save(os.path.join(path, image.filename))

def _save_video( path, video):
    _clear_dir(path)
    if not os.path.exists(path):
        os.makedirs(path)
    video.save(os.path.join(path, 'project.mp4'))

def _clear_dir( dir):
    folder = dir  # Replace with the actual path to your folder
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # Delete regular files or symbolic links
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # Recursively delete subdirectories
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

        