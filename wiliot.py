import json
import logging

from wiliot_api.platform.platform import PlatformClient


class wiliot_client:
    '''
    Class to hold wiliot configuration information and wrap around client object.
    '''
    def __init__(self, url, api_key, username, max_pixels=500):
        self.url = url
        self.username = username
        self.client = PlatformClient(api_key=api_key, owner_id=username)
        self.max_pixels = max_pixels
    

    def get_pixels(self, max_pixels=500):
        '''
        This function grabs pixels from the client, implementing a maximum pixel count.
        '''
        pixels = self.client.get_pixels()
        while pixels[1] and len(pixels[0] <= max_pixels):
            next_pixels = self.client.get_pixels(next=pixels[1])
            pixels[0] += next_pixels[0]
            pixels[1] = next_pixels[1]

        return pixels
        

    def get_asset(self, asset_id=None):
        # TODO: Consider switching to null results and logging over raising value errors
        if not asset_id:
            raise ValueError("Must provide asset ID to retrieve individual assets!")
        
        return self.client.get_asset(asset_id)


    def get_assets(self, max_assets=500):
        # TODO: Error checking
        assets = self.client.get_assets()
        return assets
