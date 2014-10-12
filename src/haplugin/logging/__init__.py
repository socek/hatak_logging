import logging.config

from hatak.plugin import Plugin


class LoggingPlugin(Plugin):

    def before_config(self):
        logging.config.fileConfig(
            self.settings['paths:logging:config'],
            disable_existing_loggers=False)
