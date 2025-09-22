class plane:
    # uçak diye bir sınıf oluşturduk. sonrasında uçakların özelliklerini yani nesneleri belirliyoruz
    # bundan sonra uçak oluşturmak istediğimiz zaman tüm özellikleri önceden belirlenmiş uçakları çat
    # diye oluşturabiliyoruz

    def __init__(self, id, position):
        self.id = id
        self.position = (0, 0, 0)

    # constructor bu

    def begin_fly(self, position):
        self.position = position
        # x ileri geri
        # y sağ sol
        # z yukarı aşağı
        # (x, y, z) şeklinde koordinatlar

    def go_forward(self, position):
        self.position = (x, 0, 0)  # normalde y ve z için self'li bir şeyler kullanıyormuşuz ama basite kaçtık

    def end_fly(self, position):
        self.position = position

    def show(self):
        print('Plane {}, coordinates on {} now'.format(self.id, self.position))


ucak1 = plane('u1', (0, 0, 0))
siha1 = plane("s1", (0, 0, 0))
iha1 = plane("i1", (0, 0, 0)) # gri görünen alanlar pycharm'ın kendi eklediği şeyler. normalde biz eklemiyoruz


class filo:
    def __init__(self):
        self.planes = []
        # filo bir array olduğu için tanımlarken bir array olarak oluşturduk biz de

    def add_to_filo (self, plane):
        self.planes.append(plane) # append ekle olarak kullanılıyor. bilmemiz gerek :)

    def show(self):
        for i in self.planes:
            print("Our filo has {} ".format(i.id))

filo2 = filo()
