#
# Building a Docker Image with
# the Latest Ubuntu Version and
# Basic Python Install
# 
# Python for Algorithmic Trading
# (c) Dr. Yves J. Hilpisch
# The Python Quants GmbH
#
# Put this file and install.sh in the same folder.
# Then execute on the command line e.g.:
#
#   docker build . -t ubuntu:basic
#
# If successful, you can then e.g. do:
#
#   docker run -h test -p 9999:9999 ubuntu:basic
#
# In the Docker container, start Jupyter e.g. by:
#
#   jupyter notebook --allow-root --ip 0.0.0.0 --port 9999
# 

# latest Ubuntu version
FROM ubuntu:latest  

# information about maintainer
MAINTAINER yves

# add the bash script
ADD install.sh /
# change rights for the script
RUN chmod u+x /install.sh
# run the bash script
RUN /install.sh
# prepend the new path
ENV PATH /root/miniconda3/bin:$PATH

# execute Bash when container is run
CMD ["/bin/bash"]