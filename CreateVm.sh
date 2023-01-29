echo "veuillez entrer le nom de votre machine virtuelle"
read vm

echo $vm

echo "veuillez entrer l'adresse ip de votre machine virtuelle"
read ip

echo $ip

function ConfigureVM()
{
  echo "configuration de la machine vm"
  sudo xen-create-image --hostname $vm --force --ip $ip --vcpus 10 --pygrub --dist bionic

}

ConfigureVM vm ip

function CreateVm()
{
  echo "creation de la machine virtuelle"
  sudo xl create -c /etc/xen/$vm.cfg
}

CreateVm vm

