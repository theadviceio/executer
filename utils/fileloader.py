import subprocess
import shlex
import mimetypes
import falcon
import utils.logs

# pylint: disable=logging-not-lazy,no-self-use


class FileLoader(object):

    def on_get(self, req, resp, file_path=None, dir_path=None):
        # pylint: disable=unused-argument
        if dir_path is None and file_path is None:
            filename = "html/index.html"
        elif dir_path is None:
            filename = "html/%s" % file_path
        else:
            filename = "html/%s/%s" % (dir_path, file_path)
        try:
            with file(filename) as file_content:
                respound = file_content.read()
            resp.body = respound
            resp.status = falcon.HTTP_200
            # TODO: mimetypes.guess_type
            try:
                content_type = mimetypes.guess_type(filename)[0]
                resp.content_type = content_type
            # pylint: disable=broad-except,invalid-name
            except Exception as e:
                utils.logs.debug("detect mimetypes faild because %s" % e)
                if filename.endswith('html') or filename.endswith('htm'):
                    resp.content_type = 'text/html'
                if filename.endswith('js') or filename.endswith('css'):
                    resp.content_type = 'text/plain'
                else:
                    cmd = shlex.split('file --mime-type {0}'.format(filename))
                    result = subprocess.check_output(cmd)
                    mime_type = result.split()[-1]
                    resp.content_type = mime_type
        # pylint: disable=broad-except,invalid-name
        except Exception as e:
            utils.logs.debug("Can't find file because %s" % e)
            #resp.body ="error"
            resp.content_type = 'text/html'
            resp.body = '''<!DOCTYPE HTML>
            <html lang="en-US">
            <head profile="http://gmpg.org/xfn/11">
            <title>Error 404: Not Found</title>
            <meta charset="UTF-8" />
            </head>
            <body>
            <h2 class="page-subtitle">The page you are looking for was not found.</h2>
            <img src="/html/jpeg/404.jpeg">
            </body>
            </html>
            '''
            resp.status = falcon.HTTP_404
