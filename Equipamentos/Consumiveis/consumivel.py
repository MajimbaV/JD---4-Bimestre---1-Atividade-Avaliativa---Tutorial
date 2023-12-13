class Consumivel():
	def __init__ (self, MANA, Nome, Descricao):
		self.MANA = MANA
		self.Nome = Nome
		self.Descricao = Descricao



pocao_hp = Consumivel(MANA = 20, Nome = "Poção de HP", Descricao = "Poção para recuperar o hp")

pocao_sp_atack = Consumivel(MANA = 0, Nome = "Atack super", Descricao = "Atack mais forte")


