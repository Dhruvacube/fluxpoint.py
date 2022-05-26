from .paths import Gifs, Images, NSFW, Misc, Welcome

class FluxpointClient(Gifs, Images, NSFW, Misc, Welcome):
    '''The fluxpoint client where all the api routes are located'''

    def __str__(self) -> str:
        return f'<Fluxpoint Client api_token={self.api_token}>'
