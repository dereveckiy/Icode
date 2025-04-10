from typing import Dict

ISO_4480_83_TABLE: Dict[float, Dict[int, float]] = {
    1: {
        4: 0.001, 5: 0.002, 6: 0.003, 7: 0.004, 8: 0.006, 9: 0.007, 10: 0.009, 11: 0.01, 
        12: 0.012, 13: 0.014, 14: 0.017, 15: 0.019, 16: 0.021, 17: 0.024, 18: 0.027, 19: 0.03, 
        20: 0.033, 21: 0.036, 22: 0.04, 23: 0.043, 24: 0.047, 25: 0.051, 26: 0.055, 27: 0.059, 
        28: 0.064, 29: 0.068, 30: 0.073, 31: 0.078, 32: 0.083, 33: 0.088, 34: 0.093, 35: 0.099, 
        36: 0.105, 37: 0.11, 38: 0.116, 39: 0.123, 40: 0.129, 41: 0.135, 42: 0.142, 43: 0.149, 
        44: 0.156, 45: 0.163, 46: 0.17, 47: 0.177, 48: 0.185, 49: 0.192, 50: 0.2, 51: 0.208, 
        52: 0.216, 53: 0.225, 54: 0.233, 55: 0.242, 56: 0.251, 57: 0.26, 58: 0.269, 59: 0.278, 
        60: 0.287, 61: 0.297, 62: 0.307, 63: 0.317, 64: 0.327, 65: 0.337, 66: 0.347, 67: 0.358, 
        68: 0.369, 69: 0.379, 70: 0.39, 71: 0.402, 72: 0.413, 73: 0.424, 74: 0.436, 75: 0.448, 
        76: 0.46, 77: 0.472, 78: 0.484, 79: 0.496
    },
    1.5:{4:0.003, 5:0.004, 6:0.005, 7:0.007, 8:0.009, 9:0.011, 10:0.014, 11:0.016, 12:0.019, 
        13:0.022, 14:0.026, 15:0.029, 16:0.033, 17:0.037, 18:0.041, 19:0.046, 20:0.051, 21:0.056,
        22:0.061, 23:0.066, 24:0.072, 25:0.078, 26:0.084, 27:0.091, 28:0.097, 29:0.104, 30:0.111, 
        31:0.119, 32:0.126, 33:0.134, 34:0.142, 35:0.151, 36:0.159, 37:0.168, 38:0.177, 39:0.186, 
        40:0.196, 41:0.205, 42:0.215, 43:0.225, 44:0.236, 45:0.247, 46:0.257, 47:0.269, 48:0.28, 
        49:0.292, 50:0.303, 51:0.316, 52:0.328, 53:0.34, 54:0.353, 55:0.366, 56:0.379, 57:0.393,
        58:0.407, 59:0.421, 60:0.435, 61:0.449, 62:0.464, 63:0.479, 64:0.494, 65:0.509, 66:0.525, 
        67:0.541, 68:0.557, 69:0.573, 70:0.59, 71:0.606, 72:0.624, 73:0.641, 74:0.658, 75:0.676,
        76:0.694, 77:0.712, 78:0.731, 79:0.749},
    
    2: {4: 0.004, 5: 0.006, 6: 0.008, 7: 0.01, 8: 0.013, 9: 0.016, 10: 0.019, 11: 0.023,
        12: 0.027, 13: 0.031, 14: 0.035, 15: 0.04, 16: 0.045, 17: 0.051, 18: 0.057, 19: 0.063,
        20: 0.069, 21: 0.076, 22: 0.083, 23: 0.09, 24: 0.098, 25: 0.106, 26: 0.115, 27: 0.123,
        28: 0.132, 29: 0.141, 30: 0.151, 31: 0.161, 32: 0.171, 33: 0.182, 34: 0.192, 35: 0.204,
        36: 0.215, 37: 0.227, 38: 0.239, 39: 0.251, 40: 0.264, 41: 0.277, 42: 0.29, 43: 0.304,
        44: 0.318, 45: 0.332, 46: 0.347, 47: 0.362, 48: 0.377, 49: 0.393, 50: 0.409, 51: 0.425,
        52: 0.441, 53: 0.458, 54: 0.475, 55: 0.493, 56: 0.51, 57: 0.528, 58: 0.547, 59: 0.565,
        60: 0.584, 61: 0.604, 62: 0.623, 63: 0.643, 64: 0.664, 65: 0.684, 66: 0.705, 67: 0.726,
        68: 0.748, 69: 0.77, 70: 0.792, 71: 0.814, 72: 0.837, 73: 0.86, 74: 0.884, 75: 0.907,
        76: 0.931, 77: 0.956, 78: 0.98, 79: 1.005},
    
    2.5: {4: 0.005, 5: 0.008, 6: 0.01, 7: 0.013, 8: 0.017, 9: 0.021, 10: 0.025, 11: 0.029,
          12: 0.034, 13: 0.04, 14: 0.046, 15: 0.052, 16: 0.058, 17: 0.065, 18: 0.073, 19: 0.081,
          20: 0.089, 21: 0.097, 22: 0.106, 23: 0.115, 24: 0.125, 25: 0.135, 26: 0.146, 27: 0.157,
          28: 0.168, 29: 0.18, 30: 0.192, 31: 0.204, 32: 0.217, 33: 0.23, 34: 0.244, 35: 0.258,
          36: 0.272, 37: 0.287, 38: 0.302, 39: 0.318, 40: 0.334, 41: 0.35, 42: 0.367, 43: 0.384,
          44: 0.402, 45: 0.42, 46: 0.438, 47: 0.457, 48: 0.476, 49: 0.496, 50: 0.516, 51: 0.536,
          52: 0.557, 53: 0.578, 54: 0.599, 55: 0.621, 56: 0.644, 57: 0.666, 58: 0.689, 59: 0.713,
          60: 0.737, 61: 0.761, 62: 0.786, 63: 0.811, 64: 0.836, 65: 0.862, 66: 0.888, 67: 0.915,
          68: 0.942, 69: 0.969, 70: 0.997, 71: 1.025, 72: 1.054, 73: 1.083, 74: 1.112, 75: 1.142,
          76: 1.172, 77: 1.202, 78: 1.233, 79: 1.265},
    
    3: {4: 0.007, 5: 0.01, 6: 0.013, 7: 0.017, 8: 0.021, 9: 0.026, 10: 0.031, 11: 0.037,
        12: 0.043, 13: 0.05, 14: 0.057, 15: 0.064, 16: 0.072, 17: 0.081, 18: 0.09, 19: 0.099,
        20: 0.109, 21: 0.119, 22: 0.13, 23: 0.141, 24: 0.153, 25: 0.165, 26: 0.178, 27: 0.191,
        28: 0.205, 29: 0.219, 30: 0.234, 31: 0.249, 32: 0.264, 33: 0.28, 34: 0.297, 35: 0.314,
        36: 0.331, 37: 0.349, 38: 0.368, 39: 0.386, 40: 0.406, 41: 0.426, 42: 0.446, 43: 0.467,
        44: 0.488, 45: 0.509, 46: 0.532, 47: 0.554, 48: 0.577, 49: 0.601, 50: 0.625, 51: 0.649,
        52: 0.674, 53: 0.7, 54: 0.726, 55: 0.752, 56: 0.779, 57: 0.806, 58: 0.834, 59: 0.862,
        60: 0.891, 61: 0.92, 62: 0.95, 63: 0.98, 64: 1.011, 65: 1.042, 66: 1.074, 67: 1.106,
        68: 1.138, 69: 1.171, 70: 1.205, 71: 1.238, 72: 1.273, 73: 1.308, 74: 1.343, 75: 1.379,
        76: 1.415, 77: 1.452, 78: 1.489, 79: 1.527},
    
    3.5: {4: 0.009, 5: 0.013, 6: 0.017, 7: 0.021, 8: 0.026, 9: 0.032, 10: 0.038, 11: 0.045,
          12: 0.052, 13: 0.06, 14: 0.068, 15: 0.077, 16: 0.087, 17: 0.097, 18: 0.107, 19: 0.118,
          20: 0.13, 21: 0.142, 22: 0.155, 23: 0.168, 24: 0.182, 25: 0.197, 26: 0.212, 27: 0.227,
          28: 0.243, 29: 0.26, 30: 0.277, 31: 0.295, 32: 0.313, 33: 0.332, 34: 0.351, 35: 0.371,
          36: 0.392, 37: 0.413, 38: 0.434, 39: 0.456, 40: 0.479, 41: 0.502, 42: 0.526, 43: 0.55,
          44: 0.575, 45: 0.601, 46: 0.627, 47: 0.653, 48: 0.68, 49: 0.708, 50: 0.736, 51: 0.765,
          52: 0.794, 53: 0.824, 54: 0.854, 55: 0.885, 56: 0.917, 57: 0.949, 58: 0.981, 59: 1.014,
          60: 1.048, 61: 1.082, 62: 1.117, 63: 1.152, 64: 1.188, 65: 1.225, 66: 1.262, 67: 1.299,
          68: 1.337, 69: 1.376, 70: 1.415, 71: 1.455, 72: 1.495, 73: 1.536, 74: 1.577, 75: 1.619,
          76: 1.662, 77: 1.705, 78: 1.748, 79: 1.792},
    
    4: {4: 0.011, 5: 0.015, 6: 0.02, 7: 0.025, 8: 0.031, 9: 0.038, 10: 0.045, 11: 0.053,
        12: 0.062, 13: 0.071, 14: 0.08, 15: 0.091, 16: 0.102, 17: 0.113, 18: 0.126, 19: 0.139,
        20: 0.152, 21: 0.166, 22: 0.181, 23: 0.196, 24: 0.212, 25: 0.229, 26: 0.246, 27: 0.264,
        28: 0.283, 29: 0.302, 30: 0.322, 31: 0.342, 32: 0.363, 33: 0.385, 34: 0.407, 35: 0.43,
        36: 0.454, 37: 0.478, 38: 0.503, 39: 0.528, 40: 0.554, 41: 0.581, 42: 0.608, 43: 0.636,
        44: 0.665, 45: 0.694, 46: 0.724, 47: 0.754, 48: 0.785, 49: 0.817, 50: 0.849, 51: 0.882,
        52: 0.916, 53: 0.95, 54: 0.985, 55: 1.021, 56: 1.057, 57: 1.094, 58: 1.131, 59: 1.169,
        60: 1.208, 61: 1.247, 62: 1.287, 63: 1.327, 64: 1.368, 65: 1.41, 66: 1.453, 67: 1.496,
        68: 1.539, 69: 1.584, 70: 1.629, 71: 1.674, 72: 1.72, 73: 1.767, 74: 1.815, 75: 1.863,
        76: 1.911, 77: 1.961, 78: 2.011, 79: 2.061},
    
    4.5: {4: 0.014, 5: 0.019, 6: 0.024, 7: 0.03, 8: 0.037, 9: 0.045, 10: 0.053, 11: 0.062,
          12: 0.072, 13: 0.082, 14: 0.093, 15: 0.105, 16: 0.118, 17: 0.131, 18: 0.145, 19: 0.16,
          20: 0.175, 21: 0.191, 22: 0.208, 23: 0.225, 24: 0.244, 25: 0.262, 26: 0.282, 27: 0.302,
          28: 0.323, 29: 0.345, 30: 0.368, 31: 0.391, 32: 0.415, 33: 0.439, 34: 0.464, 35: 0.49,
          36: 0.517, 37: 0.544, 38: 0.573, 39: 0.601, 40: 0.631, 41: 0.661, 42: 0.692, 43: 0.724,
          44: 0.756, 45: 0.789, 46: 0.823, 47: 0.857, 48: 0.892, 49: 0.928, 50: 0.965, 51: 1.002,
          52: 1.04, 53: 1.079, 54: 1.118, 55: 1.158, 56: 1.199, 57: 1.241, 58: 1.283, 59: 1.326,
          60: 1.37, 61: 1.414, 62: 1.459, 63: 1.505, 64: 1.551, 65: 1.598, 66: 1.646, 67: 1.695,
          68: 1.744, 69: 1.794, 70: 1.845, 71: 1.896, 72: 1.948, 73: 2.001, 74: 2.055, 75: 2.109,
          76: 2.164, 77: 2.22, 78: 2.276, 79: 2.333},
    
    5: {4: 0.017, 5: 0.022, 6: 0.028, 7: 0.035, 8: 0.043, 9: 0.052, 10: 0.061, 11: 0.072,
        12: 0.083, 13: 0.094, 14: 0.107, 15: 0.12, 16: 0.134, 17: 0.149, 18: 0.165, 19: 0.182,
        20: 0.199, 21: 0.217, 22: 0.236, 23: 0.255, 24: 0.276, 25: 0.297, 26: 0.319, 27: 0.342,
        28: 0.365, 29: 0.39, 30: 0.415, 31: 0.441, 32: 0.467, 33: 0.495, 34: 0.523, 35: 0.552,
        36: 0.582, 37: 0.613, 38: 0.644, 39: 0.676, 40: 0.709, 41: 0.743, 42: 0.778, 43: 0.813,
        44: 0.849, 45: 0.886, 46: 0.924, 47: 0.962, 48: 1.001, 49: 1.041, 50: 1.082, 51: 1.124,
        52: 1.166, 53: 1.21, 54: 1.254, 55: 1.298, 56: 1.344, 57: 1.39, 58: 1.437, 59: 1.485,
        60: 1.534, 61: 1.583, 62: 1.634, 63: 1.685, 64: 1.737, 65: 1.789, 66: 1.843, 67: 1.897,
        68: 1.952, 69: 2.008, 70: 2.064, 71: 2.121, 72: 2.18, 73: 2.238, 74: 2.298, 75: 2.359,
        76: 2.42, 77: 2.482, 78: 2.545, 79: 2.608},
    
    5.5: {4: 0.02, 5: 0.026, 6: 0.033, 7: 0.041, 8: 0.05, 9: 0.06, 10: 0.07, 11: 0.082,
          12: 0.094, 13: 0.107, 14: 0.121, 15: 0.136, 16: 0.152, 17: 0.168, 18: 0.186, 19: 0.204,
          20: 0.224, 21: 0.244, 22: 0.265, 23: 0.286, 24: 0.309, 25: 0.333, 26: 0.357, 27: 0.382,
          28: 0.408, 29: 0.435, 30: 0.463, 31: 0.492, 32: 0.522, 33: 0.552, 34: 0.583, 35: 0.616,
          36: 0.649, 37: 0.683, 38: 0.717, 39: 0.753, 40: 0.789, 41: 0.827, 42: 0.865, 43: 0.904,
          44: 0.944, 45: 0.985, 46: 1.027, 47: 1.069, 48: 1.113, 49: 1.157, 50: 1.202, 51: 1.248,
          52: 1.295, 53: 1.343, 54: 1.391, 55: 1.441, 56: 1.491, 57: 1.542, 58: 1.594, 59: 1.647,
          60: 1.701, 61: 1.756, 62: 1.811, 63: 1.867, 64: 1.925, 65: 1.983, 66: 2.042, 67: 2.102,
          68: 2.162, 69: 2.224, 70: 2.286, 71: 2.35, 72: 2.414, 73: 2.479, 74: 2.545, 75: 2.611,
          76: 2.679, 77: 2.747, 78: 2.817, 79: 2.887},
    
    6: {4: 0.023, 5: 0.03, 6: 0.038, 7: 0.047, 8: 0.057, 9: 0.068, 10: 0.08, 11: 0.092,
        12: 0.106, 13: 0.121, 14: 0.136, 15: 0.153, 16: 0.17, 17: 0.188, 18: 0.208, 19: 0.228,
        20: 0.249, 21: 0.271, 22: 0.295, 23: 0.319, 24: 0.344, 25: 0.369, 26: 0.396, 27: 0.424,
        28: 0.453, 29: 0.483, 30: 0.513, 31: 0.545, 32: 0.577, 33: 0.611, 34: 0.645, 35: 0.68,
        36: 0.717, 37: 0.754, 38: 0.792, 39: 0.831, 40: 0.871, 41: 0.912, 42: 0.954, 43: 0.997,
        44: 1.041, 45: 1.086, 46: 1.131, 47: 1.178, 48: 1.226, 49: 1.274, 50: 1.324, 51: 1.374,
        52: 1.425, 53: 1.478, 54: 1.531, 55: 1.585, 56: 1.64, 57: 1.696, 58: 1.753, 59: 1.811,
        60: 1.87, 61: 1.93, 62: 1.991, 63: 2.053, 64: 2.115, 65: 2.179, 66: 2.244, 67: 2.309,
        68: 2.376, 69: 2.443, 70: 2.511, 71: 2.581, 72: 2.651, 73: 2.722, 74: 2.794, 75: 2.867,
        76: 2.941, 77: 3.016, 78: 3.092, 79: 3.169},
    
    6.5: {4: 0.027, 5: 0.035, 6: 0.044, 7: 0.054, 8: 0.065, 9: 0.077, 10: 0.09, 11: 0.104,
          12: 0.119, 13: 0.135, 14: 0.152, 15: 0.17, 16: 0.189, 17: 0.209, 18: 0.231, 19: 0.253,
          20: 0.276, 21: 0.3, 22: 0.325, 23: 0.352, 24: 0.379, 25: 0.407, 26: 0.437, 27: 0.467,
          28: 0.499, 29: 0.531, 30: 0.564, 31: 0.599, 32: 0.634, 33: 0.671, 34: 0.708, 35: 0.747,
          36: 0.786, 37: 0.827, 38: 0.869, 39: 0.911, 40: 0.955, 41: 1, 42: 1.045, 43: 1.092,
          44: 1.14, 45: 1.188, 46: 1.238, 47: 1.289, 48: 1.341, 49: 1.394, 50: 1.448, 51: 1.502,
          52: 1.558, 53: 1.615, 54: 1.673, 55: 1.732, 56: 1.792, 57: 1.853, 58: 1.915, 59: 1.978,
          60: 2.042, 61: 2.107, 62: 2.174, 63: 2.241, 64: 2.309, 65: 2.378, 66: 2.448, 67: 2.519,
          68: 2.592, 69: 2.665, 70: 2.739, 71: 2.814, 72: 2.891, 73: 2.968, 74: 3.046, 75: 3.126,
          76: 3.206, 77: 3.288, 78: 3.37, 79: 3.454},
    
    7: {4: 0.031, 5: 0.04, 6: 0.05, 7: 0.061, 8: 0.073, 9: 0.086, 10: 0.1, 11: 0.116,
        12: 0.132, 13: 0.15, 14: 0.168, 15: 0.188, 16: 0.209, 17: 0.231, 18: 0.254, 19: 0.278,
        20: 0.304, 21: 0.33, 22: 0.357, 23: 0.386, 24: 0.416, 25: 0.447, 26: 0.478, 27: 0.511,
        28: 0.546, 29: 0.581, 30: 0.617, 31: 0.654, 32: 0.693, 33: 0.732, 34: 0.773, 35: 0.815,
        36: 0.858, 37: 0.902, 38: 0.947, 39: 0.993, 40: 1.04, 41: 1.089, 42: 1.138, 43: 1.189,
        44: 1.24, 45: 1.293, 46: 1.347, 47: 1.402, 48: 1.458, 49: 1.515, 50: 1.574, 51: 1.633,
        52: 1.693, 53: 1.755, 54: 1.818, 55: 1.881, 56: 1.946, 57: 2.012, 58: 2.079, 59: 2.148,
        60: 2.217, 61: 2.287, 62: 2.359, 63: 2.431, 64: 2.505, 65: 2.58, 66: 2.656, 67: 2.733,
        68: 2.811, 69: 2.89, 70: 2.97, 71: 3.051, 72: 3.134, 73: 3.217, 74: 3.302, 75: 3.388,
        76: 3.475, 77: 3.563, 78: 3.652, 79: 3.742},
    
    7.5: {4: 0.035, 5: 0.045, 6: 0.056, 7: 0.068, 8: 0.081, 9: 0.096, 10: 0.111, 11: 0.128,
          12: 0.146, 13: 0.165, 14: 0.186, 15: 0.207, 16: 0.23, 17: 0.254, 18: 0.279, 19: 0.305,
          20: 0.332, 21: 0.361, 22: 0.391, 23: 0.422, 24: 0.454, 25: 0.487, 26: 0.521, 27: 0.557,
          28: 0.594, 29: 0.632, 30: 0.671, 31: 0.711, 32: 0.753, 33: 0.796, 34: 0.839, 35: 0.884,
          36: 0.931, 37: 0.978, 38: 1.027, 39: 1.077, 40: 1.127, 41: 1.18, 42: 1.233, 43: 1.287,
          44: 1.343, 45: 1.4, 46: 1.458, 47: 1.517, 48: 1.578, 49: 1.639, 50: 1.702, 51: 1.766,
            52: 1.831, 53: 1.897, 54: 1.965, 55: 2.033, 56: 2.103, 57: 2.174, 58: 2.246, 59: 2.319,
            60: 2.394, 61: 2.47, 62: 2.546, 63: 2.625, 64: 2.704, 65: 2.784, 66: 2.866, 67: 2.949,
            68: 3.032, 69: 3.118, 70: 3.204, 71: 3.291, 72: 3.38, 73: 3.47, 74: 3.561, 75: 3.653,
            76: 3.746, 77: 3.841, 78: 3.937, 79: 4.034},
    
    8: {4: 0.04, 5: 0.051, 6: 0.063, 7: 0.076, 8: 0.09, 9: 0.106, 10: 0.123, 11: 0.141,
        12: 0.161, 13: 0.182, 14: 0.204, 15: 0.227, 16: 0.251, 17: 0.277, 18: 0.304, 19: 0.332,
        20: 0.362, 21: 0.393, 22: 0.425, 23: 0.458, 24: 0.493, 25: 0.528, 26: 0.565, 27: 0.604,
        28: 0.643, 29: 0.684, 30: 0.726, 31: 0.77, 32: 0.814, 33: 0.86, 34: 0.907, 35: 0.956,
        36: 1.005, 37: 1.056, 38: 1.108, 39: 1.162, 40: 1.216, 41: 1.272, 42: 1.33, 43: 1.388,
        44: 1.448},
    
    8.5: {4: 0.045, 5: 0.057, 6: 0.07, 7: 0.084, 8: 0.1, 9: 0.117, 10: 0.136, 11: 0.155,
          12: 0.176, 13: 0.199, 14: 0.222, 15: 0.247, 16: 0.274, 17: 0.301, 18: 0.33, 19: 0.361,
          20: 0.393, 21: 0.426, 22: 0.46, 23: 0.496, 24: 0.533, 25: 0.571, 26: 0.611, 27: 0.652,
          28: 0.694, 29: 0.738, 30: 0.783, 31: 0.83, 32: 0.877, 33: 0.926, 34: 0.977, 35: 1.028,
          36: 1.082, 37: 1.136, 38: 1.192, 39: 1.249, 40: 1.307, 41: 1.367, 42: 1.428, 43: 1.49,
          44: 1.554},
    
    9: {4: 0.051, 5: 0.064, 6: 0.078, 7: 0.093, 8: 0.11, 9: 0.129, 10: 0.149, 11: 0.17,
        12: 0.192, 13: 0.216, 14: 0.242, 15: 0.269, 16: 0.297, 17: 0.327, 18: 0.358, 19: 0.39,
        20: 0.424, 21: 0.46, 22: 0.496, 23: 0.535, 24: 0.574, 25: 0.615, 26: 0.658, 27: 0.701,
        28: 0.747, 29: 0.793, 30: 0.841, 31: 0.891, 32: 0.942, 33: 0.994, 34: 1.048, 35: 1.103,
        36: 1.159, 37: 1.217, 38: 1.277, 39: 1.338, 40: 1.4, 41: 1.463, 42: 1.528, 43: 1.595,
        44: 1.663},
    
    9.5: {4: 0.057, 5: 0.071, 6: 0.086, 7: 0.103, 8: 0.121, 9: 0.141, 10: 0.162, 11: 0.185,
          12: 0.209, 13: 0.235, 14: 0.262, 15: 0.291, 16: 0.321, 17: 0.353, 18: 0.386, 19: 0.421,
          20: 0.457, 21: 0.495, 22: 0.534, 23: 0.575, 24: 0.617, 25: 0.66, 26: 0.706, 27: 0.752,
          28: 0.8, 29: 0.85, 30: 0.901, 31: 0.954, 32: 1.008, 33: 1.063, 34: 1.112, 35: 1.179,
          36: 1.239, 37: 1.301, 38: 1.364, 39: 1.428, 40: 1.494, 41: 1.562, 42: 1.631, 43: 1.701,
          44: 1.773},
    }


    # ... Остальные наборы коэффициентов (2, 2.5, 3, 3.5, ... 9.5)


def get_volume(diameter_cm, length_m, table_grade: float = 1) -> float:
    """
    Вычисляет объем древесины по методу ISO 4480-83 с использованием таблицы ГОСТ.
    
    Параметры:
      diameter_cm: Диаметр в сантиметрах.
      length_m:    Длина в метрах.
      table_grade: Ключ для выбора набора коэффициентов в таблице (например, 1, 1.5, 2, ...). По умолчанию 1.
    
    Алгоритм:
      1. Выбирается таблица коэффициентов по table_grade.
      2. Округляется диаметр до ближайшего целого.
      3. Если диаметр меньше минимального значения в таблице – берется минимальное,
         если больше максимального – максимальное, иначе выбирается ближайший ключ.
      4. Получается коэффициент (factor) из таблицы.
      5. Расчитывается объем: volume = factor * length_m.
    """
    try:
        table = ISO_4480_83_TABLE[table_grade]
    except KeyError:
        raise ValueError(f"Набор коэффициентов для значения {table_grade} не найден в таблице ISO_4480_83_TABLE")
    
    d_val = int(round(float(diameter_cm)))
    keys = sorted(table.keys())
    d = min(keys, key=lambda k: abs(k - d_val))
    
    factor = table.get(d)
    # Добавляем отладочный вывод, чтобы увидеть какие значения вычисляются
    print(f"DEBUG: diameter_cm={diameter_cm}, d_val={d_val}, выбранный ключ d={d}, коэффициент factor={factor}")
    
    if factor is None:
        raise ValueError(f"Нет данных для диаметра {d} см в таблице для набора {table_grade}")
    
    volume = factor
    return volume