FROM ubuntu:24.04
# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages and fix package errors
RUN apt-get update \
    && apt-get install -y sudo openssh-server net-tools cryptsetup>
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && dpkg --configure -a \
    && apt-get install -f -y

# Create user for Tenant1
ARG USERNAME=tenant1
RUN useradd -m -s /bin/bash $USERNAME && \
    echo "$USERNAME:tenant@123" | chpasswd && \
    usermod -aG sudo $USERNAME

# Set the default command
CMD ["/bin/bash"]
