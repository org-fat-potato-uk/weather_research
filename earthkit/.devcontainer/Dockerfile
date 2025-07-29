FROM mcr.microsoft.com/devcontainers/anaconda:1-3

# Copy environment.yml (if found) to a temp location so we update the environment.
COPY environment.yml* /tmp/conda-tmp/
RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then umask 0002 && /opt/conda/bin/conda env update -n base -f /tmp/conda-tmp/environment.yml; fi \
    && rm -rf /tmp/conda-tmp
COPY .devcontainer/.bashrc /home/vscode/.bashrc