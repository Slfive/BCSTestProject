from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .models import Block


def main(request):
	 url_blocks = 'https://bcschain.info/api/blocks/'
	 blockS_res = requests.get(url_blocks)
	 blockS_res_js = blockS_res.json() 
	 all_blocks_info = []
	 for block in blockS_res_js: 
	 	block_info = {

	 	'hash': block["hash"],
	 	'height': block["height"], 
	 	'time': block["timestamp"],
	 	'miner_adress': block["miner"], 
	 	'transactions_quantity': block["transactionCount"],

	 	} 
	 	Block.objects.create(height_block = block_info["height"], hash_block = block_info["hash"], time_block  = block_info["time"], miner_adress = block_info["miner_adress"], quantity= block_info["transactions_quantity"] )
	 all_blocks_res = Block.objects.all()


	 context = {'all_info': all_blocks_res}
	 return render(request, 'bcsChain/index.html', context)


