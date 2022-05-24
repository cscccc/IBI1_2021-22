import xml.sax
import matplotlib.pyplot as plt
import time

terms = {}
dfs_set = set()

class Gene:
	def __init__(self):
		self.ID = None
		self.defstr = None
		self.is_a = []
		self.sub = 0
		self.sub_trans = 0

class GeneHandler(xml.sax.ContentHandler):
	def __init__(self):
		self.cur = ''
		self.content = []
		self.interm = False
		self.gene = None
	def startElement(self, tag, attributes):
		self.cur = tag
		if tag == 'term':
			self.gene = Gene()
			self.interm = True
	def endElement(self, tag):
		if self.interm:
			if self.cur == 'id':
				self.gene.ID = ''.join(self.content)
			elif self.cur == 'defstr':
				self.gene.defstr = ''.join(self.content)
			elif self.cur == 'is_a':
				self.gene.is_a.append(''.join(self.content))
			elif tag == 'term':
				global terms
				terms[self.gene.ID] = self.gene
				self.gene = None
				self.interm = False
			self.content.clear()
		self.cur = ''
	def characters(self, content):
		if self.interm:
			if self.cur=='id' or self.cur=='defstr' or self.cur=='is_a':
				self.content.append(content)

def node_sum(ID, add, add_trans):
	global dfs_set, terms
	for prev in terms[ID].is_a:
		if prev not in dfs_set:
			terms[prev].sub += add
			terms[prev].sub_trans += add_trans
			dfs_set.add(prev)
			node_sum(prev, add ,add_trans)

if __name__ == "__main__":
	benchmark_str = f"=====[Benchmark] %s cost %d ms, total cost %d ms====="
	benchmark_start = time.time()
	parser = xml.sax.make_parser()
	parser.setFeature(xml.sax.handler.feature_namespaces, 0)
	parser.setContentHandler(GeneHandler())
	parser.parse("go_obo.xml")
	benchmark_stage1 = time.time()
	print(benchmark_str % ("Reading xml file",(benchmark_stage1-benchmark_start)*1000,(benchmark_stage1-benchmark_start)*1000))
	print("There are", len(terms), "terms in go_obo.xml")

	for ID in terms:
		dfs_set.clear()
		#node_sum(ID, terms[ID].sub+1, terms[ID].sub_trans+(1 if terms[ID].defstr.find("translation") != -1 else 0))
		node_sum(ID, 1, 1 if terms[ID].defstr.find("translation") != -1 else 0)
	
	Sum = []
	SumT = []
	for ID in terms:
		Sum.append(terms[ID].sub)
		SumT.append(terms[ID].sub_trans)
	benchmark_stage2 = time.time()
	print(benchmark_str % ("Calculating childnodes",(benchmark_stage2-benchmark_stage1)*1000,(benchmark_stage2-benchmark_start)*1000))

	plt.subplot(1,2,1)
	plt.boxplot(Sum,vert=True, whis=1.5, patch_artist=True, showbox=True, showcaps=True, showfliers=True)
	plt.title('Distribution of child node number of all GO terms')
	plt.xlabel("all GO terms")
	plt.ylabel("Number")
	plt.subplot(1,2,2)
	plt.boxplot(SumT,vert=True, whis=1.5, patch_artist=True, showbox=True, showcaps=True, showfliers=True)
	plt.title('Distribution of child node number of terms associated with ‘translation’')
	plt.xlabel("associated with ‘translation’")
	plt.ylabel("Number")
	benchmark_stage3 = time.time()
	print(benchmark_str % ("Generating figures",(benchmark_stage3-benchmark_stage2)*1000,(benchmark_stage3-benchmark_start)*1000))
	plt.show()