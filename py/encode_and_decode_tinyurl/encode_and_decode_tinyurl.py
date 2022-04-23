import hashlib
class Codec:
    d = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = hashlib.md5(str(longUrl).encode("utf-8")).digest()
        if key in self.d:
          return key

        self.d[key] = longUrl
        return key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl in self.d:
          return self.d[shortUrl]