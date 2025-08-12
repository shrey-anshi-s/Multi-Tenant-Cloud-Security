FROM ubuntu:24.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install required packages
RUN apt-get update && \
    apt-get install -y sudo openssh-server net-tools cryptsetup curl gnupg2 vim apt-utils && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    dpkg --configure -a && \
    apt-get install -f -y

# Add user
ARG USERNAME=tenant1
RUN useradd -m -s /bin/bash $USERNAME && \
    echo "$USERNAME:tenant@123" | chpasswd && \
    usermod -aG sudo $USERNAME

# Start SSH service
RUN mkdir /var/run/sshd
EXPOSE 22

# Default command
CMD ["/bin/bash"]

