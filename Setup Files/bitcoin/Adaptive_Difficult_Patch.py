@@ Source: https://github.com/jramos/p2pool/commit/e44dc19dada6a346628d838fa9261cd1872f493e

@@ -210,7 +210,7 @@ def upnp_thread():
        
        print 'Listening for workers on %r port %i...' % (worker_endpoint[0], worker_endpoint[1])
        
        wb = work.WorkerBridge(node, my_pubkey_hash, args.donation_percentage, merged_urls, args.worker_fee)
        wb = work.WorkerBridge(node, my_pubkey_hash, args.donation_percentage, merged_urls, args.worker_fee, args.diff_policy)
        web_root = web.get_web_root(wb, datadir_path, bitcoind_getinfo_var)
        caching_wb = worker_interface.CachingWorkerBridge(wb)
        worker_interface.WorkerInterface(caching_wb).attach_to(web_root, get_handler=lambda request: request.redirect('static/'))
@@ -424,7 +424,9 @@ def run():
    worker_group.add_argument('-f', '--fee', metavar='FEE_PERCENTAGE',
        help='''charge workers mining to their own bitcoin address (by setting their miner's username to a bitcoin address) this percentage fee to mine on your p2pool instance. Amount displayed at http://127.0.0.1:WORKER_PORT/fee (default: 0)''',
        type=float, action='store', default=0, dest='worker_fee')
    
    worker_group.add_argument('-d', '--difficulty', metavar='DIFFICULTY',
        help='''set difficulty policy: D - default, A - adaptive, F - force adaptive (ignore miner's request)''',
        type=str, action='store', default='D', dest='diff_policy')
    bitcoind_group = parser.add_argument_group('bitcoind interface')
    bitcoind_group.add_argument('--bitcoind-config-path', metavar='BITCOIND_CONFIG_PATH',
        help='custom configuration file path (when bitcoind -conf option used)',
