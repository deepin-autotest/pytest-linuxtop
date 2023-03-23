# -*- coding: utf-8 -*-
from multiprocessing import Process
from os import makedirs, system
from os.path import exists
from time import strftime

top_cmd = "top -b -d 3 -w 512"


def pytest_addoption(parser):
    group = parser.getgroup('linuxtop')
    group.addoption(
        '--top',
        action='store',
        dest='top',
        default='',
        help='过程中记录top命令中的值'
    )


def pytest_sessionstart(session):
    if session.config.option.top:
        def record_top():
            top_log_path = f"/tmp/logs"
            if not exists(top_log_path):
                makedirs(top_log_path)
            system(
                f"{top_cmd} | grep ^top -A {int(session.config.option.top) + 6} > "
                f'{top_log_path}/top_{strftime("%Y%m%d%H%M%S")}.log'
            )

        session.p = Process(target=record_top, args=())
        session.p.start()


def pytest_sessionfinish(session):
    if not session.config.option.collectonly and session.config.option.top:
        session.p.terminate()
        system(
            f"ps -aux | grep '{top_cmd}' | cut -c 9-15 | xargs kill -9 > /dev/null 2>&1"
        )
        session.p.close()
