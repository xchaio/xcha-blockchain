from enum import Enum


class ProtocolMessageTypes(Enum):
    # Shared protocol (all services)
    handshake = 12

    # Harvester protocol (harvester <-> farmer)
    harvester_handshake = 13
    new_proof_of_space = 14
    request_signatures = 15
    respond_signatures = 16

    # Farmer protocol (farmer <-> full_node)
    new_signage_point = 17
    declare_proof_of_space = 18
    request_signed_values = 19
    signed_values = 20
    farming_info = 21

    # Timelord protocol (timelord <-> full_node)
    new_peak_timelord = 22
    new_unfinished_block_timelord = 23
    new_infusion_point_vdf = 24
    new_signage_point_vdf = 25
    new_end_of_sub_slot_vdf = 26
    request_compact_proof_of_time = 27
    respond_compact_proof_of_time = 28

    # Full node protocol (full_node <-> full_node)
    new_peak = 29
    new_transaction = 30
    request_transaction = 31
    respond_transaction = 32
    request_proof_of_weight = 33
    respond_proof_of_weight = 34
    request_block = 35
    respond_block = 36
    reject_block = 37
    request_blocks = 38
    respond_blocks = 39
    reject_blocks = 40
    new_unfinished_block = 41
    request_unfinished_block = 42
    respond_unfinished_block = 43
    new_signage_point_or_end_of_sub_slot = 44
    request_signage_point_or_end_of_sub_slot = 45
    respond_signage_point = 46
    respond_end_of_sub_slot = 47
    request_mempool_transactions = 48
    request_compact_vdf = 49
    respond_compact_vdf = 50
    new_compact_vdf = 51
    request_peers = 52
    respond_peers = 53

    # Wallet protocol (wallet <-> full_node)
    request_puzzle_solution = 54
    respond_puzzle_solution = 55
    reject_puzzle_solution = 56
    send_transaction = 57
    transaction_ack = 58
    new_peak_wallet = 59
    request_block_header = 60
    respond_block_header = 61
    reject_header_request = 62
    request_removals = 63
    respond_removals = 64
    reject_removals_request = 65
    request_additions = 66
    respond_additions = 67
    reject_additions_request = 68
    request_header_blocks = 69
    reject_header_blocks = 70
    respond_header_blocks = 71

    # Introducer protocol (introducer <-> full_node)
    request_peers_introducer = 72
    respond_peers_introducer = 73

    # Simulator protocol
    farm_new_block = 74

    # New harvester protocol
    new_signage_point_harvester = 75
    request_plots = 76
    respond_plots = 77
