FROM ubuntu:22.04 AS base

FROM disconnect3d/nsjail

COPY --from=base / /jail/

# Global flag
COPY flag /jail/flag
COPY oldgame /jail/

COPY start.sh /start.sh
RUN chmod +x /start.sh

CMD [ "/start.sh" ]