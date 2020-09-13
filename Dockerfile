#
# Building a Docker Image with
# the Latest Ubuntu Version and
# Basic Python Install
#
# docker build . -t ubuntu:basic
# docker run -h test -p 9999:9999 ubuntu:basic

# latest Ubuntu version
FROM ubuntu:latest  

# information about maintainer
MAINTAINER fester

# add the bash script
ADD install.sh get_historical_pandas.py helpers.py /
# change rights for the script
RUN chmod u+x /install.sh
# run the bash script
RUN /install.sh
# prepend the new path
ENV PATH /root/miniconda3/bin:$PATH

# execute Bash when container is run
CMD ["/bin/bash"]
