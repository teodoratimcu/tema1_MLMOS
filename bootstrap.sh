#/bin/bash
echo "bootstrap.sh is running"

echo "Updating system software"
yum -y update


if grep -q SELINUX="disabled" /etc/selinux/config; then
	echo "SELINUX is disabled"
fi

setenforce 0
