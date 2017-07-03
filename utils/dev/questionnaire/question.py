#coding=utf-8

questions = {
	1:"Qual é o seu sexo?",
	2:"Qual é o seu estado civil?", 
	3:"Qual é a sua cor ou raça?", 
	4:"Indique a distância entre o seu local de procedência e o local onde pretendearealizar o seu curso de graduação USP.", 
	5:"Onde você cursou o ensino fundamental?", 
	6:"Onde você cursou o ensino médio?", 
	7:"Que tipo de curso de ensino médio você concluiu ou concluirá?", 
	8:"Em que turno você cursou o ensino médio?", 
	9:"Você frequenta ou frequentou cursinho pré-vestibular?", 
	10:"Você já iniciou ou está frequentando algum curso superior?",
	11:"Somando a renda bruta de todas as pessoas que moram com você, quanto é a renda familiar mensal? (Some todas as rendas que sustentam a família)", 
	12:"Quantas pessoas da família vivem da renda indicada na pergunta anterior?", 
	13:"Quantas pessoas contribuem para a obtenção dessa renda familiar?", 
	14:"Qual é o nível de instrução de seu pai ou responsável?", 
	15:"Qual é o nível de instrução de sua mãe ou responsável?", 
	16:"Você exerce alguma atividade remunerada?", 
	17:"Onde você acessa a internet com maior frequência?", 
	18:"Quanto à manutenção mensal de sua família, assinale a situação ocupacional do principal contribuinte (ou sua, no caso de independência financeira).", 
	19:"Indique a situação do imóvel em que sua família ou você (no caso de independência da família) reside atualmente.", 
	20:"Sua família ou você (no caso de independênciaafinanceira) possui propriedades além do imóvel ondeareside? Quantas?", 
	21:"Como pretende se manter durante seus estudos universitários?", 
	22:"Quantos carros existem em sua casa?", 
	23:"Quantos computadores existem em sua casa?", 
	24:"No ano passado, você se inscreveu como “treineiro” na FUVEST?", 
	25:"Além do vestibular da FUVEST, você pretende se inscrever também em outro vestibular?", 
	26:"Além do vestibular da FUVEST, você pretende se inscrever também em outro vestibular?", 
	27:"Em algum dos vestibulares que você já prestou na FUVEST, chegou a ser convocado para matrícula?", 
	28:"Você optou pelo PASUSP?", 
	29:"Você está participando do processo INCLUSP?", 
	30:"Você solicitou bônus INCLUSP-EB?", 
	31:"Você solicitou bônus INCLUSP-PPI?", 
	32:"Qual sua idade em 3112/2015?",
	33:"Para os candidatos que cursaram todo o Ensino Médio em Escolas Públicas: Qual é a sua cor ou raça?", 
	34:"Para os candidatos que cursaram todo o Ensino Médio em Escolas Públicas: Onde você cursou o ensino fundamental?" 
}

answers_1 = {
	1:'Masculino.',
	2:'Feminino.',
}
answers_2 = {
	1:'Solteiro.',
	2:'Em união estável/casado.',
	3:'Desquitado, separado ou divorciado.',
	4:'Viúvo.',
}
answers_3 = {
	1:'Branca.',
	2:'Preta.',
	3:'Parda.',
	4:'Amarela.',
	5:'Indígena.',
}
answers_4 = {
	1:'Abaixo de 11 km.',
	2:'Entre 11 e 30 km.',
	3:'Entre 31 e 60 km.',
	4:'Entre 61 e 80 km.',
	5:'Entre 81 e 100 km.',
	6:'Entre 101 e 300 km.',
	7:'Acima de 300 km.',
}
answers_5 = {
	1:'Todo em escola pública.',
	2:'Todo em escola particular.',
	3:'Maior parte em escola pública.',
	4:'Maior parte em escola particular.',
	5:'No exterior.',
	6:'Em outra situação (Escola particular com bolsa, Fundações, SESI, SENAI).',
}
answers_6 = {
	1:'Todo em escola pública.',
	2:'Todo em escola particular.',
	3:'Maior parte em escola pública.',
	4:'Maior parte em escola particular.',
	5:'No exterior.',
	6:'Em outra situação (Escola particular com bolsa, Fundações, SESI, SENAI).',
}
answers_7 = {
	1:'Ensino médio comum.',
	2:'Curso técnico (Industrial, Eletrônica, Química etc).',
	3:'Curso para magistério (antigo Normal).',
	4:'Educação de jovens e adultos (EJA).',
	5:'Certificação do Ensino Médio pelo ENEM.',
	6:'Outro.',
}
answers_8 = {
	1:'Diurno (só manhã ou só tarde).',
	2:'Diurno integral (manhã e tarde).',
	3:'Noturno.',
	4:'Maior parte no diurno.',
	5:'Maior parte no noturno.',
	6:'Outro turno.',
}
answers_9 = {
	1:'Não.',
	2:'Sim, intensivo de seis meses.',
	3:'Sim, durante um ano.',
	4:'Sim, já é o segundo ano em que frequento cursinho.',
	5:'Sim, já frequento há mais de dois anos.',
}
answers_10 = {
	1:'Não.',
	2:'Sim, mas o abandonei.',
	3:'Sim, mas irei abandoná-lo se passar neste vestibular.',
	4:'Sim, estou cursando e pretendo fazer os dois.',
	5:'Sim, e já o concluí.',
}
answers_11 = {
	1:'Inferior a 1 SM.',
	2:'Entre 1 e 2 SM.',
	3:'Entre 2 e 3 SM.',
	4:'Entre 3 e 5 SM.',
	5:'Entre 5 e 7 SM.',
	6:'Entre 7 e 10 SM.',
	7:'Entre 10 e 15 SM.',
	8:'Entre 15 e 20 SM.',
	9:'Acima de 20 SM.',
}
answers_12 = {
	1:'Uma.',
	2:'Duas.',
	3:'Três.',
	4:'Quatro.',
	5:'Cinco.',
	6:'Seis ou mais.',
}
answers_13 = {
	1:'Uma.',
	2:'Duas.',
	3:'Três.',
	4:'Quatro ou mais.',
}
answers_14 = {
	1:'Não estudou.',
	2:'Ensino fundamental incompleto.',
	3:'Ensino fundamental completo.',
	4:'Ensino médio incompleto.',
	5:'Ensino médio completo.',
	6:'Ensino superior incompleto.',
	7:'Ensino superior completo.',
	8:'Pós-graduação incompleta.',
	9:'Pós-graduação completa.',
}
answers_15 = {
	1:'Não estudou.',
	2:'Ensino fundamental incompleto.',
	3:'Ensino fundamental completo.',
	4:'Ensino médio incompleto.',
	5:'Ensino médio completo.',
	6:'Ensino superior incompleto.',
	7:'Ensino superior completo.',
	8:'Pós-graduação incompleta.',
	9:'Pós-graduação completa.',
}
answers_16 = {
	1:'Não.',
	2:'Sim, eventual.',
	3:'Sim, regularmente, em tempo parcial.',
	4:'Sim, regularmente, em tempo integral.',
}
answers_17 = {
	1:'Em casa.',
	2:'Em casa de amigos.',
	3:'No trabalho.',
	4:'Na escola ou no cursinho.',
	5:'No centro comunitário.',
	6:'Em lan houses.',
	7:'Em outro local.',
	8:'Não acesso.',
}
answers_18 = {
	1:'Proprietário de empresa grande ou média.',
	2:'Proprietário de pequena ou microempresa.',
	3:'Assalariado com contrato formal (empresa pública ou privada).',
	4:'Profissional liberal (que exerce atividade compatívelacom formação universitária) ou trabalhando por ...',
	5:'Bolsa de estudo, estágio ou monitoria.',
	6:'Vive exclusivamente de rendimentos de aluguéis e/ou de investimentos financeiros.',
	7:'Aposentado ou pensionista.',
	8:'No momento, não exerce atividade remunerada nemarecebe pensão ou aposentadoria (desemprego até 12 meses).',
	9:'Trabalho eventual (exercício do trabalho sem a garantia de continuidade ou vínculo).',
	10:'Atividade agropecuária (não proprietário, meeiro,aarrendatário).',
	11:'Outra.',
}
answers_19 = {
	1:'Próprio, quitado.',
	2:'Cedido por instituição/empresa/parentes/conhecidos.',
	3:'Próprio, com financiamento em curso.',
	4:'Alugado.',
	5:'Próprio, construído em terreno sem regularização.',
}
answers_20 = {
	1:'Nenhuma.',
	2:'Uma.',
	3:'Duas.',
	4:'Três.',
	5:'Quatro ou mais.',
}
answers_21 = {
	1:'Somente com recursos dos pais.',
	2:'Trabalhando, mas contando, para o essencial, com os recursos da família.',
	3:'Trabalhando para participar do rateio das despesas da família.',
	4:'Por conta própria, com recursos oriundos de trabalho remunerado.',
	5:'Com bolsa de estudos ou crédito educativo.',
	6:'Com bolsa ou crédito educativo, trabalhando e contando, ainda, com o apoio da família.',
	7:'Outros.',
}
answers_22 = {
	1:'Nenhum.',
	2:'Um.',
	3:'Dois.',
	4:'Três.',
	5:'Quatro.',
	6:'Cinco ou mais.',
}
answers_23 = {
	1:'Nenhum.',
	2:'Um.',
	3:'Dois.',
	4:'Três.',
	5:'Quatro ou mais.',
}
answers_24 = {
	1:'Sim.',
	2:'Não.',
}
answers_25 = {
	1:'Sim, da UNICAMP.',
	2:'Sim, da UNESP.',
	3:'Sim, da UNICAMP e da UNESP.',
	4:'Sim, de outras universidades, mas não no da UNICAMP nem no da UNESP.',
	5:'Não pretendo me inscrever em nenhum outro vestibular.',
}
answers_26 = {
	1:'Nenhum.',
	2:'Um.',
	3:'Dois.',
	4:'Três.',
	5:'Quatro ou mais.',
}
answers_27 = {
	1:'Não.',
	2:'Sim, mas não efetuei a matrícula.',
	3:'Efetuei a matrícula, mas abandonei o curso.',
	4:'Ainda estou fazendo o curso no qual me matriculei.',
	5:'Já concluí o curso no qual me matriculei.',
	6:'Nunca prestei nenhum vestibular na FUVEST.',
}
answers_28 = {
	1:'Sim',
	2:'Não',
}
answers_29 = {
	1:'Sim',
	2:'Não',
}
answers_30 = {
	1:'Sim',
	2:'Não',
}
answers_31 = {
	1:'Sim',
	2:'Não',
}
answers_32 = {
	1:'Até 16 anos',
	2:'17 anos',
	3:'18 anos',
	4:'19 anos',
	5:'20 anos',
	6:'21 anos',
	7:'de 22 a 25 anos',
	8:'Acima de 25 anos',
}
answers_33 = {
	1:'Branca.',
	2:'Preta.',
	3:'Parda.',
	4:'Amarela.',
	5:'Indígena.',
}
answers_34 = {
	1:'Todo em escola pública.',
	2:'Todo em escola particular.',
	3:'Maior parte em escola pública.',
	4:'Maior parte em escola particular.',
	5:'No exterior.',
	6:'Em outra situação (Escola particular com bolsa, Fundações, SESI, SENAI).',
}

answers = {
	1:answers_1,
	2:answers_2,
	3:answers_3,
	4:answers_4,
	5:answers_5,
	6:answers_6,
	7:answers_7,
	8:answers_8,
	9:answers_9,
	10:answers_10,
	11:answers_11,
	12:answers_12,
	13:answers_13,
	14:answers_14,
	15:answers_15,
	16:answers_16,
	17:answers_17,
	18:answers_18,
	19:answers_19,
	20:answers_20,
	21:answers_21,
	22:answers_22,
	23:answers_23,
	24:answers_24,
	25:answers_25,
	26:answers_26,
	27:answers_27,
	28:answers_28,
	29:answers_29,
	30:answers_30,
	31:answers_31,
	32:answers_32,
	33:answers_33,
	34:answers_34,
}

def getInstance():
	query = list()
	for i in range(34):
		print i+1, questions[i+1], '\n'
		for j in range( len( answers[i+1] ) ):
			print '\t', j, answers[i+1][j+1]
		opt = raw_input()
		print '\n\n'
		query.append( opt )
	return query

if __name__ == "__getInstance__":
	main()
