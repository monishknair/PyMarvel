# -*- coding: utf-8 -*-

__author__ = 'Garrett Pennington'
__date__ = '02/07/14'

from .core import MarvelObject, DataWrapper, DataContainer, List, Summary, TextObject, Image
 

class ComicDataWrapper(DataWrapper):
    @property
    def data(self):
        return ComicDataContainer(self.marvel, self.dict['data'])

class ComicDataContainer(DataContainer):
    @property
    def results(self):
        return self.list_to_instance_list(self.dict['results'], Comic)

class Comic(MarvelObject):
    """
    Comic object
    Takes a dict of character attrs
    """
    _resource_url = 'comics'


    @property
    def id(self):
        return self.dict['id']

    @property
    def digitalId(self):
        return int(self.dict['digitalId'])

    @property
    def title(self):
        return self.dict['title']

    @property
    def issueNumber(self):
        return float(self.dict['issueNumber'])

    @property
    def variantDescription(self):
        return self.dict['description']

    @property
    def description(self):
        """
        :returns:  str -- The preferred description of the comic.
        """
        return self.dict['description']

    @property
    def modified(self):
        return str_to_datetime(self.dict['modified'])

    @property
    def modified_raw(self):
        return self.dict['modified']

    @property
    def isbn(self):
        return self.dict['isbn']

    @property
    def upc(self):
        return self.dict['upc']

    @property
    def diamondCode(self):
        return self.dict['diamondCode']

    @property
    def ean(self):
        return self.dict['ean']

    @property
    def issn(self):
        return self.dict['issn']

    @property
    def format(self):
        return self.dict['format']

    @property
    def pageCount(self):
        return int(self.dict['pageCount'])

    @property
    def textObjects(self):
        """
        :returns: list -- List of TextObjects
        """
        return self.list_to_instance_list(self.dict['textObjects'], TextObject)

    @property
    def resourceURI(self):
        return self.dict['resourceURI']

    @property
    def urls(self):
        return self.dict['urls']

    @property
    def series(self):
        return self.dict['series']

    @property
    def variants(self):
        """
        Returns List of ComicSummary objects
        """
        return self.list_to_instance_list(self.dict['variants'], ComicSummary)
                    
    @property
    def collections(self):
        """
        Returns List of ComicSummary objects
        """
        return self.list_to_instance_list(self.dict['collections'], ComicSummary)

    @property
    def collectedIssues(self):
        """
        Returns List of ComicSummary objects
        """
        return self.list_to_instance_list(self.dict['collectedIssues'], ComicSummary)

    @property
    def dates(self):
        return self.list_to_instance_list(self.dict['dates'], ComicDate)

    @property
    def prices(self):
        return self.list_to_instance_list(self.dict['prices'], ComicPrice)

    @property
    def thumbnail(self):
        return Image(self.marvel, self.dict['thumbnail'])

    @property
    def images(self):
        return self.list_to_instance_list(self.dict['images'], Image)

    @property
    def creators(self):
        from .creator import CreatorList
        return CreatorList(self.marvel, self.dict['creators'])

    @property
    def characters(self):
        from .character import CharacterList
        return CharacterList(self.marvel, self.dict['characters'])

    @property
    def stories(self):
        from .story import StoryList
        return StoryList(self.marvel, self.dict['stories'])
        
    @property
    def events(self):
        from .event import EventList
        return EventList(self.marvel, self.dict['events'])
        
        
    def get_creators(self, *args, **kwargs):
        """
        Returns a full CreatorDataWrapper object for this character.

        /comics/{comicId}/creators

        :returns:  CreatorDataWrapper -- A new request to API. Contains full results set.
        """
        from .creator import Creator, CreatorDataWrapper
        url = "%s/%s/%s" % (Comic.resource_url(), self.id, Creator.resource_url())
        response = json.loads(self.marvel._call(url, self.marvel._params(kwargs)).text)
        return CreatorDataWrapper(self, response)

    def get_characters(self, *args, **kwargs):
        """
        Returns a full CharacterDataWrapper object for this character.

        /comics/{comicId}/characters

        :returns:  CreatorDataWrapper -- A new request to API. Contains full results set.
        """
        from .character import Character, CharacterDataWrapper
        url = "%s/%s/%s" % (Comic.resource_url(), self.id, Character.resource_url())
        response = json.loads(self.marvel._call(url, self.marvel._params(kwargs)).text)
        return CharacterDataWrapper(self, response)



class ComicList(List):
    """
    ComicList object
    """

    @property
    def items(self):
        """
        Returns List of ComicSummary objects
        """
        return self.list_to_instance_list(self.dict['items'], ComicSummary)

class ComicSummary(Summary):
    """
    CommicSummary object
    """

class ComicDate(MarvelObject):
    """
    ComicDate object
    """
    @property
    def type(self):
        return self.dict['type']

    @property
    def date(self):
        return self.str_to_datetime(self.dict['date'])

class ComicPrice(MarvelObject):
    """
    ComicPrice object
    """
    @property
    def type(self):
        return self.dict['type']

    @property
    def price(self):
        return float(self.dict['price'])
