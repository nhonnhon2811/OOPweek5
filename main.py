class Device:
    def __init__(self, matb,tentb,namsd,giamua,trangthai):
        self.__matb = matb
        self.tentb = tentb
        while namsd > 2026:
            print("Năm sử dụng không hợp lệ, vui lòng nhập lại")
            namsd = int(input("Nhập lại năm sử dụng: "))
        self.namsd = namsd
        while giamua < 0:
            print("Giá mua không hợp lệ, vui lòng nhập lại")
            giamua = float(input("Nhập lại giá mua: "))
        self.giamua = giamua
        self.trangthai = trangthai
    def chiphibaotri(self):
        pass
    def __str__(self):
        return f"Mã thiết bị: {self.__matb}, Tên thiết bị: {self.tentb}, Năm sử dụng: {self.namsd}, Giá mua: {self.giamua}, Trạng thái: {self.trangthai}"   
    def get_matb(self):
        return self.__matb  
class Computer(Device):
    def __init__(self, ram,cpu,gpu, matb, tentb, namsd, giamua, trangthai):
        super().__init__(matb, tentb, namsd, giamua, trangthai)
        self.ram = ram
        self.cpu = cpu
        self.gpu = False
        if gpu:
            self.gpu = True
        
    def chiphibaotri(self):
        self.chiphibaotri = self.giamua * 0.05
        if self.gpu:
            self.chiphibaotri += self.giamua * 0.02
        if 2026 - self.namsd > 5:
            self.chiphibaotri += self.giamua * 0.01
        return self.chiphibaotri
class Printer(Device):
    def __init__(self, loaiin, sotrang,inmau, hotromang, matb, tentb, namsd, giamua, trangthai):
        super().__init__(matb, tentb, namsd, giamua, trangthai)
        self.loaiin = loaiin
        self.sotrang = sotrang
        self.inmau = inmau# bo sung them thuoc tinh in mau vi chiphibaotri can dieu kien in mau
        self.hotromang = hotromang
    def chiphibaotri(self):
        self.chiphibaotri = self.giamua * 0.04
        if self.sotrang>100000 :
            self.chiphibaotri += 500000
        if self.inmau:
            self.chiphibaotri += 300000
        return self.chiphibaotri
class Projector(Device):
    def __init__(self, dosang,giosd, matb, tentb, namsd, giamua, trangthai):
        super().__init__(matb, tentb, namsd, giamua, trangthai)
        self.dosang = dosang
        self.giosd = giosd
    def chiphibaotri(self):
        self.chiphibaotri = self.giamua * 0.04
        if self.giosd > 3000 :
            self.chiphibaotri += 1500000
        return self.chiphibaotri    
class Inetworkable:
    def __init__(self):
        self.__ip = None
        self.__isconected = False
    def Connect(self, ip):
        self.__ip = ip
        self.__isconected = True
    def Disconnect(self):
        self.__ip = None
        self.__isconected = False
    def get_ip(self):
        return self.__ip
    def is_connected(self):
        return self.__isconected
class Labroom:
    def __init__(self, malab, tenlab, succhua):
        self.malab = malab
        self.tenlab = tenlab
        self.succhua = succhua
        self.devices = []
    def add_device(self, device):
        while device == None:
                    print("Thiết bị không hợp lệ, vui lòng nhập lại.")
                    device = input("Nhập thiết bị: ")
        for d in self.devices:
            if d.get_matb() == device.get_matb():
                print("Thiết bị đã tồn tại trong phòng thí nghiệm.")
                return
        self.devices.append(device)
    def remove_device(self, matb):
        b = False
        for device in self.devices:
            if device.get_matb() == matb:
                self.devices.remove(device)
                b = True
                break
        return b
    def FindDevice(self, matb):
        for device in self.devices:
            if device.get_matb() == matb:
                return device
        return None
    def Tongchiphibaotri(self):
        total_cost = 0
        for device in self.devices:
            total_cost += device.chiphibaotri()
        return total_cost
    def danhsachthietbibaotri(self):  
        list = []
        for device in self.devices:
            if device.trangthai == "Đang bảo trì" or 2026 - device.namsd > 5:
                list.append(device)
        return list

pc1 = Computer("16GB", "Intel i7", "RTX 5050Ti", "PC001", "Máy tính 1", 2020, 15000000, "Đang hoạt động")
pc2 = Computer("8GB", "Intel i5", "", "PC002", "Máy tính 2", 2021, 10000000, "Đang hoạt động")
pr1 = Printer("Laser", 120000, True, True, "PR001", "Máy in 1", 2018, 5000000, "Đang hoạt động")
pr2 = Printer("Phun", 80000, False, False, "PR002", "Máy in 2", 2022, 3000000, "Đang hoạt động")
projector = Projector(3000, 4000, "PJ001", "Máy chiếu 1", 2019, 8000000, "Đang hoạt động")

lab1 = Labroom("LAB001", "Phòng thí nghiệm 1", 10)
lab2 = Labroom("LAB002", "Phòng thí nghiệm 2", 5)

lab1.add_device(pc1)
lab1.add_device(pr1)
lab1.add_device(pc1)

lab2.add_device(pc2)
lab2.add_device(pr2)
lab2.add_device(projector)

print("Danh sách thiết bị trong phòng thí nghiệm 1:")
for device in lab1.devices:
    print(f"- {device}")

print("\nDanh sách thiết bị trong phòng thí nghiệm 2:")
for device in lab2.devices:
    print(f"- {device}")

print(f"\nTổng chi phí bảo trì trong phòng thí nghiệm 1: {lab1.Tongchiphibaotri()}")
print(f"Tổng chi phí bảo trì trong phòng thí nghiệm 2: {lab2.Tongchiphibaotri()}")

for d in lab1.danhsachthietbibaotri():
    print(f"Thiết bị cần bảo trì trong phòng thí nghiệm 1: {d}")

for d in lab2.danhsachthietbibaotri():
    print(f"Thiết bị cần bảo trì trong phòng thí nghiệm 2: {d}")


