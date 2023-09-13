# -*- coding: utf-8 -*-
from werkzeug._internal import _log
from werkzeug.serving import _ansi_style


def log_style(msg, *args, log='info', col=None):
    """
    logging style
    
    usage:
        >>> log_style('I am info log', log='info')
        >>> log_style('I am warning log', log='warning')
        >>> log_style('I am error log', log='error')
        >>> log_style('I am critical log', log='critical')


        # this two are thesame (inter-changebly), (use if text need to be bold)
        >>> log_style('I am error log of cyan(color) bold txt', 'cyan', log='error', col='bold')
        >>> log_style('I am error log of cyan(color) bold txt', 'bold', log='error', col='cyan')

        # this just change color to magenta
        >>> log_style('I am error log of magenta(color) bold txt', 'bold', log='error', col='magenta')

        NOTE: look on `werkzeug.serving.log_request` for more status
        
    by default `werkzeug._internal._log` logging level is set to debug,
    mean we only have to log with:
        INFO
        WARNING
        ERROR
        CRITICAL

        it negate:
            NOTSET
            DEBUG
    """
    
    if col == None:
        if log == 'info':
            col = 'green'
        elif log == 'warning':
            col = 'yellow'
        elif log == 'error':
            col = 'red'
        elif log == 'critical':
            col = 'cyan'
        else: # if any
            col = 'magenta'
    return _log(log, _ansi_style(msg, col, *args))
