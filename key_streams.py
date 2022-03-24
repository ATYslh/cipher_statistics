import numpy as np


def mobius_key():
    return np.array([])


def oeis_key():
    return np.array(
        [5, 50, 61, 72, 83, 94, 104, 115, 126, 137, 148, 159, 203, 214, 225, 236, 247, 258, 269, 302, 313, 324, 335, 346, 357, 368, 379, 401,
         412, 423, 434, 445, 456, 467, 478, 489, 500, 511, 522, 533, 544, 555, 566, 577, 588, 599, 610, 621, 632, 643, 654, 665, 676, 687, 698,
         720, 731, 742, 753, 764, 775, 786, 797, 830, 841, 852, 863, 874, 885, 896, 940, 951, 962, 973, 984, 995, 1040, 1051, 1062, 1073, 1084,
         1095, 1150, 1161, 1172, 1183, 1194, 1260, 1271, 1282, 1293, 1370, 1381, 1392, 1480, 1491, 1590, 2030, 2041, 2052, 2063, 2074, 2085,
         2096, 2140, 2151, 2162, 2173, 2184, 2195, 2250, 2261, 2272, 2283, 2294, 2360, 2371, 2382, 2393, 2470, 2481, 2492, 2580, 2591, 2690,
         3020, 3031, 3042, 3053, 3064, 3075, 3086, 3097, 3130, 3141, 3152, 3163, 3174, 3185, 3196, 3240, 3251, 3262, 3273, 3284, 3295, 3350,
         3361, 3372, 3383, 3394, 3460, 3471, 3482, 3493, 3570, 3581, 3592, 3680, 3691, 3790, 4010, 4021, 4032, 4043, 4054, 4065, 4076, 4087,
         4098, 4120, 4131, 4142, 4153, 4164, 4175, 4186, 4197, 4230, 4241, 4252, 4263, 4274, 4285, 4296, 4340, 4351, 4362, 4373, 4384, 4395,
         4450, 4461, 4472, 4483, 4494, 4560, 4571, 4582, 4593, 4670, 4681, 4692, 4780, 4791, 4890, 5000, 5011, 5022, 5033, 5044, 5055, 5066,
         5077, 5088, 5099, 5110, 5121, 5132, 5143, 5154, 5165, 5176, 5187, 5198, 5220, 5231, 5242, 5253, 5264, 5275, 5286, 5297, 5330, 5341,
         5352, 5363, 5374, 5385, 5396, 5440, 5451, 5462, 5473, 5484, 5495, 5550, 5561, 5572, 5583, 5594, 5660, 5671, 5682, 5693, 5770, 5781,
         5792, 5880, 5891, 5990, 6001, 6012, 6023, 6034, 6045, 6056, 6067, 6078, 6089, 6100, 6111, 6122, 6133, 6144, 6155, 6166, 6177, 6188,
         6199, 6210, 6221, 6232, 6243, 6254, 6265, 6276, 6287, 6298, 6320, 6331, 6342, 6353, 6364, 6375, 6386, 6397, 6430, 6441, 6452, 6463,
         6474, 6485, 6496, 6540, 6551, 6562, 6573, 6584, 6595, 6650, 6661, 6672, 6683, 6694, 6760, 6771, 6782, 6793, 6870, 6881, 6892, 6980,
         6991, 7002, 7013, 7024, 7035, 7046, 7057, 7068, 7079, 7101, 7112, 7123, 7134, 7145, 7156, 7167, 7178, 7189, 7200, 7211, 7222, 7233,
         7244, 7255, 7266, 7277, 7288, 7299, 7310, 7321, 7332, 7343, 7354, 7365, 7376, 7387, 7398, 7420, 7431, 7442, 7453, 7464, 7475, 7486,
         7497, 7530, 7541, 7552, 7563, 7574, 7585, 7596, 7640, 7651, 7662, 7673, 7684, 7695, 7750, 7761, 7772, 7783, 7794, 7860, 7871, 7882,
         7893, 7970, 7981, 7992, 8003, 8014, 8025, 8036, 8047, 8058, 8069, 8102, 8113, 8124, 8135, 8146, 8157, 8168, 8179, 8201, 8212, 8223,
         8234, 8245, 8256, 8267, 8278, 8289, 8300, 8311, 8322, 8333, 8344, 8355, 8366, 8377, 8388, 8399, 8410, 8421, 8432, 8443, 8454, 8465,
         8476, 8487, 8498, 8520, 8531, 8542, 8553, 8564, 8575, 8586, 8597, 8630, 8641, 8652, 8663, 8674, 8685, 8696, 8740, 8751, 8762, 8773,
         8784, 8795, 8850, 8861, 8872, 8883, 8894, 8960, 8971, 8982, 8993, 9004, 9015, 9026, 9037, 9048, 9059, 9103, 9114, 9125, 9136, 9147,
         9158, 9169, 9202, 9213, 9224, 9235, 9246, 9257, 9268, 9279, 9301, 9312, 9323, 9334, 9345, 9356, 9367, 9378, 9389, 9400, 9411, 9422,
         9433, 9444, 9455, 9466, 9477, 9488, 9499, 9510, 9521, 9532, 9543, 9554, 9565, 9576, 9587, 9598, 9620, 9631, 9642, 9653, 9664, 9675,
         9686, 9697, 9730, 9741, 9752, 9763, 9774, 9785, 9796, 9840, 9851, 9862, 9873, 9884, 9895, 9950, 9961, 9972, 9983, 9994, 10004, 10015,
         10026, 10037, 10048, 10059, 10103, 10114, 10125, 10136, 10147, 10158, 10169, 10202, 10213, 10224, 10235, 10246, 10257, 10268, 10279,
         10301, 10312, 10323, 10334, 10345, 10356, 10367, 10378, 10389, 10400, 10411, 10422, 10433, 10444, 10455, 10466, 10477, 10488, 10499,
         10510, 10521, 10532, 10543, 10554, 10565, 10576, 10587, 10598, 10620, 10631, 10642, 10653, 10664, 10675, 10686, 10697, 10730, 10741,
         10752, 10763, 10774, 10785, 10796, 10840, 10851, 10862, 10873, 10884, 10895, 10950, 10961, 10972, 10983, 10994, 11005, 11016, 11027,
         11038, 11049, 11104, 11115, 11126, 11137, 11148, 11159, 11203, 11214, 11225, 11236, 11247, 11258, 11269, 11302, 11313, 11324, 11335,
         11346, 11357, 11368, 11379, 11401, 11412, 11423, 11434, 11445, 11456, 11467, 11478, 11489, 11500, 11511, 11522, 11533, 11544, 11555,
         11566, 11577, 11588, 11599, 11610, 11621, 11632, 11643, 11654, 11665, 11676, 11687, 11698, 11720, 11731, 11742, 11753, 11764, 11775,
         11786, 11797, 11830, 11841, 11852, 11863, 11874, 11885, 11896, 11940, 11951, 11962, 11973, 11984, 11995, 12006, 12017, 12028, 12039,
         12105, 12116, 12127, 12138, 12149, 12204, 12215, 12226, 12237, 12248, 12259, 12303, 12314, 12325, 12336, 12347, 12358, 12369, 12402,
         12413, 12424, 12435, 12446, 12457, 12468, 12479, 12501, 12512, 12523, 12534, 12545, 12556, 12567, 12578, 12589, 12600, 12611, 12622,
         12633, 12644, 12655, 12666, 12677, 12688, 12699, 12710, 12721, 12732, 12743, 12754, 12765, 12776, 12787, 12798, 12820, 12831, 12842,
         12853, 12864, 12875, 12886, 12897, 12930, 12941, 12952, 12963, 12974, 12985, 12996, 13007, 13018, 13029, 13106, 13117, 13128, 13139,
         13205, 13216, 13227, 13238, 13249, 13304, 13315, 13326, 13337, 13348, 13359, 13403, 13414, 13425, 13436, 13447, 13458, 13469, 13502,
         13513, 13524, 13535, 13546, 13557, 13568, 13579, 13601, 13612, 13623, 13634, 13645, 13656, 13667, 13678, 13689, 13700, 13711, 13722,
         13733, 13744, 13755, 13766, 13777, 13788, 13799, 13810, 13821, 13832, 13843, 13854, 13865, 13876, 13887, 13898, 13920, 13931, 13942,
         13953, 13964, 13975, 13986, 13997, 14008, 14019, 14107, 14118, 14129, 14206, 14217, 14228, 14239, 14305, 14316, 14327, 14338, 14349,
         14404, 14415, 14426, 14437, 14448, 14459, 14503, 14514, 14525, 14536, 14547, 14558, 14569, 14602, 14613, 14624, 14635, 14646, 14657,
         14668, 14679, 14701, 14712, 14723, 14734, 14745, 14756, 14767, 14778, 14789, 14800, 14811, 14822, 14833, 14844, 14855, 14866, 14877,
         14888, 14899, 14910, 14921, 14932, 14943, 14954, 14965, 14976, 14987, 14998, 15009, 15108, 15119, 15207, 15218, 15229, 15306, 15317,
         15328, 15339, 15405, 15416, 15427, 15438, 15449, 15504, 15515, 15526, 15537, 15548, 15559, 15603, 15614, 15625, 15636, 15647, 15658,
         15669, 15702, 15713, 15724, 15735, 15746, 15757, 15768, 15779, 15801, 15812, 15823, 15834, 15845, 15856, 15867, 15878, 15889, 15900,
         15911, 15922, 15933, 15944, 15955, 15966, 15977, 15988, 15999, 16109, 16208, 16219, 16307, 16318, 16329, 16406, 16417, 16428, 16439,
         16505, 16516, 16527, 16538, 16549, 16604, 16615, 16626, 16637, 16648, 16659, 16703, 16714, 16725, 16736, 16747, 16758, 16769, 16802,
         16813, 16824, 16835, 16846, 16857, 16868, 16879, 16901, 16912, 16923, 16934, 16945, 16956, 16967, 16978, 16989, 17209, 17308, 17319,
         17407])