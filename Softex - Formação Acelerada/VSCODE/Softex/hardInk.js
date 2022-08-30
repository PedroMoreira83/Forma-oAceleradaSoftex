function Hardware(type, ram, cpu, hdd) {
  this.type = type;
  this.cpu = cpu;
  this.ram = ram;
  this.hdd = hdd;
}

const hardware1 = new Hardware('PC', '2.8 Ghz', '16 GB', '256 GB');
const hardware2 = new Hardware(
  'SERVER',
  '2.8 Ghz + 2.8 Ghz',
  '128 GB',
  '4094 GB'
);

Hardware.prototype.toString = function hardwareToString() {
  var hardware = this.type + ' ' + this.cpu + ' ' + this.ram + ' ' + this.hdd;
  return hardware;
};

console.log(hardware1.toString());
console.log(hardware2.toString());
