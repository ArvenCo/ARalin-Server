from libs import *

from src.controller.project import ProjectController
stream = Blueprint('stream', __name__)

@stream.route('/video')
def video():

    full_path = f'static/uploads/{request.args.get("id")}/video/project.mp4'
    if not os.path.exists(full_path) : return "Video Not Found", 404

    range_header = request.headers.get('Range', None)
    byte1, byte2 = 0, None
    if range_header:
        match = re.search(r'(\d+)-(\d*)', range_header)
        groups = match.groups()

        if groups[0]:
            byte1 = int(groups[0])
        if groups[1]:
            byte2 = int(groups[1])
    
    chunk, start, length, file_size = ProjectController.get_chunk(request.args.get('id'),byte1, byte2)
    resp = Response(chunk, 206, mimetype='video/mp4',
                      content_type='video/mp4', direct_passthrough=True)
    resp.headers.add('Content-Range', 'bytes {0}-{1}/{2}'.format(start, start + length - 1, file_size))
    return resp