# Find my friend's information

## Challenge (??? points, ??? solves)

Some time ago, I met this person at a conference I attended with Dex.
I'd like to read his research paper again.
Dex received a photo from him...
With this photo, can you find the DOI of the research paper?
I heard that he likes to analyze and write the source code.

Flag format: CDDC2025{ }

- Replace / (slash) with \_ (underscore)
- e.g.) If DOI is 11.2222/abc.33333, then flag is CDDC2025{11.2222_abc.33333}

## Summary

- Run `exiftool` on the image file to extract metadata
- Look for the `Artist` tag in the metadata, which contains the author's name as `ws1004`
- Search for this username on [Github](https://github.com/ws1004)
- This is the paper mentioned: [https://doi.org/10.1016/j.fsidi.2023.301611](https://doi.org/10.1016/j.fsidi.2023.301611)

## Flag

`CDDC2025{10.1016_j.fsidi.2023.301611}`
