from .errors import UnmarshalError


class Detail:
    """
    A simple class to keep track of the Detail element
    """

    def __init__(self, event, elm):
        self.event = event
        self.elm = elm

    def __repr__(self):
        "<GenericDetail>"

    @property
    def marti_cs(self):
        """
        A list of callsigns in the Marti tag (if present)

        Returns an empty list if not present
        """
        if self.elm is None:
            return

        marti = self.elm.find("marti")
        if marti is None:
            return

        for dest in marti.iterfind("dest"):
            yield dest.get("callsign")

    @property
    def as_element(self):
        """
        Returns the element representation of the Detail object.

        If the Detail object was created with from_elm(), it should always
        return that exact element. Otherwise, the object should generate the
        element, and return that.
        """
        return self.elm

    @staticmethod
    def from_elm(elm, event=None):
        """
        Build a Detail object from an element, with the event for context
        """
        if elm.tag != "detail":
            raise UnmarshalError("Cannot create Detail from %s" % elm.tag)

        return Detail(event, elm)

    @property
    def uid(self):
        if not self.event:
            return None
        return self.event.uid

    @property
    def point(self):
        if not self.event:
            return None
        return self.event.point
