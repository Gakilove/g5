brief_targets = [
    'cpus\.(ipc)',
    'cpus\.committed(Insts)',
    #'cpus\.num(Cycles)'
]
ipc_target = [
    'cpus\.(ipc)',
]

flow_target = [
        'dataflow_queue\.(WKFlowUsage::\d+)',
        'dataflow_queue\.(WKFlowUsage::\w+)',
        ]

standard_targets = [
    '(numCycles)',
    'cpus\.committed(Insts)',
    'cpus\.(ipc)',
]

cache_targets = [
    '(dcache.*_m)iss_rate',
    '(icache.*_m)iss_rate',
    '(l2.*_m)iss_rate',
]

branch_targets = [
    'd?iewc?\.?(branchMispredicts)',
    'd?iewc?\.?exec_(branches)',
    # 'iew\.iewExec(LoadInsts)',
    # 'iew\.exec_(stores)',
    # 'thread(0\.squashedLoads)',
    # 'thread(0\.squashedStores)',
    # '(iqSquashedInstsIssued)',
    # '(commitSquashedInsts)',
]
fanout_targets = [
        'diewc\.(largeFanoutInsts)',
        'diewc\.(falseNegativeLF)',
        'diewc\.(falsePositiveLF)',
        'diewc\.(forwarders)Committed',
        #'diewc\.(firstLevelFw)',
        #'diewc\.(secondaryLevelFw)',
        #'diewc\.(gainFromReshape)',
        'diewc\.(reshapeContrib)',
        'diewc\.(nonCriticalForward)',
        #'diewc\.(negativeContrib)',
        'diewc\.(wkDelayedCycles)',

        'cpus\.(squashedFUTime)',
        'dataflow_queue\.(readyWaitTime)::total',
        ]

sched_targets = [
        'DQGroup\d.(oldWaitYoung)',
        'cpus\.diewc\.(meanHeadExecDistance)',
        ]

fetch_targets = [
    'cpus\.fetch\.(fetchFromLoopBuffer)',
    'cpus\.(fetch\.rate) ',
]


operand_targets = [
        # 'arch_state\.(numBusyOperands::\d)',
        'arch_state\.(numDispInsts::\d)',
        'arch_state\.(meanBusyOp_\d)',

        ]
packet_targets = [
        'dataflow_queue\.(KeySrcP)acket',
        'dataflow_queue\.(SrcOpP)ackets',
        'dataflow_queue\.(DestOpP)ackets',
        'dataflow_queue\.(MemP)ackets',
        'dataflow_queue\.(OrderP)ackets',
        'dataflow_queue\.(MiscP)ackets',
        'dataflow_queue\.(TotalP)ackets',
        ]
breakdown_targets= [
        'diewc\.(queueingD)elay',
        'diewc\.(ssrD)elay',
        'diewc\.(pendingD)elay',
        'diewc\.FU(ContentionD)elay',
        'DQTop\.(HalfSquash)es',
        ]
mem_pred_targets= [
        'system\.switch_cpus\.diewc\.(trueNegativeBypass)',
        'system\.switch_cpus\.diewc\.(truePositiveBypass)',
        'system\.switch_cpus\.diewc\.(falseNegativeBypass)',
        'system\.switch_cpus\.diewc\.(falsePositiveBypass)',
        'system\.switch_cpus\.diewc\.(FPCanceledBypass)',
        'system\.switch_cpus\.diewc\.(FPSquashedBypass)',
        'system\.switch_cpus\.diewc\.(loadReExecRate)',
        'system\.switch_cpus\.diewc\.(loadSquashRate)',
        'system\.switch_cpus\.diewc\.(verifSkipRate)',
        'system\.switch_cpus\.diewc\.(reExecutedNonBypass)',
        'system\.switch_cpus\.diewc\.(reExecutedBypass)',
        'system\.switch_cpus\.iew\.memOrder(Violation)Events',
        ]
