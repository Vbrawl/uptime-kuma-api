class UptimeKumaException(Exception):
    """
    There was an exception that occurred while communicating with Uptime Kuma.
    """


class Timeout(UptimeKumaException):
    """
    A timeout has occurred while communicating with Uptime Kuma.
    """

class UptimeKumaNoDatabase(UptimeKumaException):
    """
    The server isn't configured with a database yet, connection is impossible.
    """