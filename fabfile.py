from fabric.api import env , run
from fabric.operations import sudo

GIT_REPO = 'https://github.com/MoNaiZi/gitskills'

env.user = 'root'
env.password = 'vnLiJPI7i5o8'

env.hosts = ['zhongminyong.tech']
env.port = '28950'

def deploy():
    source_folder = '/home/zmy/sites/zhongminyong.tech/gitskills'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('restart gunicorn-zhongminyong.tech')
    sudo('service nginx reload')
