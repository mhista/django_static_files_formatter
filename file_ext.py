
"""
the form returns a string part of the media to be uploaded, which is checked against the list
of allowed media access
import 'the upload_file_to' function if you wish to control user uploads.
"""
def check_file_type(file):
    '''checks the type of file being used'''
    extensions = {
        'images' : ('jpeg', 'jpg', 'png', 'gif'),
        'videos' : ('mp4', 'webm', 'ogg'),
        'music' : ('mp4', 'mp3', 'ogg', 'wav')
    }

    file = file.split('.')[1]
    file = str(file)
    for x in extensions:
        if file in extensions[x]:
            return x
    return None

file_type = check_file_type



def check_file_extension(file):
    """
        checks the extension being used
        1.can be imported in the view function to check the file type before validating form
        2. if uploading multiple files, override the post method to, loop through the files to check the file type
    
    """

    extensions = {
        'images' : ('jpeg', 'jpg', 'png', 'gif'),
        'videos' : ('mp4', 'webm', 'ogg'),
        'music' : ('mp4', 'mp3', 'ogg', 'wav')
    }
    file = str(file)
    fil = file.split('.')[1]
    for x in extensions.values():
        if fil in x:
            return file
        return None
file_ext = check_file_extension











def uploaded_files_directory(instance,filename, file_func=file_type):
    """used by the model to create a directory for the file being used 
    """
    file = file_func(filename)
    # if file == 'vid':
    #     return f'videos/{instance.posts.author}/{filename}'
    # elif file == 'pic':
    #     return f'{instance.posts.author}/images/{filename}'
    # elif file == 'music':
    #     return f'music/{instance.posts.author}/{filename}'
    return f'{instance.posts.author}/{file}/{filename}'


# def select_storage():
#     return MyLocalStorage() if settings.DEBUG else MyRemoteStorage()

upload_file_to = uploaded_files_directory







# returns MEDIA_ROOT/user_<id>/filename
# return f'user_{instance.user.id}/{filename}'
