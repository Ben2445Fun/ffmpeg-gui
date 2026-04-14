FROM python:3.12
RUN apt update \
  && apt install -y \
  g++ gcc make sqlite3 time curl git nano dos2unix \
  net-tools iputils-ping iproute2 sudo gdb less \
  ffmpeg libgl1 libglib2.0-0 libdbus-1-3 libegl1 \
  libxcb-cursor0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 \
  libxcb-randr0 libxcb-render-util0 libxcb-shape0 \
  libxcb-xinerama0 libxcb-xkb1 libxkbcommon-x11-0 \
  && apt clean

ARG USER=user
ARG UID=1000
ARG GID=1000

ENV USER=${USER}
ENV HOME=/home/${USER}

RUN useradd -m -s /bin/bash -N -u $UID $USER && \
  echo "${USER} ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers && \
  chmod 0440 /etc/sudoers && \
  chmod g+w /etc/passwd
USER user
WORKDIR ${HOME}

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENV PATH="${HOME}/.local/bin:$PATH"
ENV PYTHONPATH="${HOME}/.local/lib/python3.12/site-packages:$PYTHONPATH"
CMD ["python", "ffmpeggui.py"]