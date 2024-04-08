
from mocoRequest import app, get_local_ip
from readConf import readConfig
from makeLog import logger

log = logger()
ip = get_local_ip()


if __name__ == '__main__':
    mocodata = readConfig(confname='moco')
    app.run(host='0.0.0.0',port=mocodata['port'],debug=False)

    log.info(log.info("程序入口为:"+"http://"+ip+":9090/moco"))

# import os
# if __name__ == '__main__':
#     log_dir = os.path.abspath('./log')
#     print(log_dir)