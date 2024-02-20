#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 09:09:49 2024

@author: Joseph Chevalier
"""

import sys, os, copy, glob
import numpy as np
import astropy
import scipy
import matplotlib.pyplot as plt

def get_infos_from_image(fits_image_path):
    return (aq_date, aq_hms, aq_cam, aq_filter, expos_time)

def load_bias_frames(path_to_bias_dir, aq_date, aq_cam):
    return bias_frames_list, bias_array

def load_dark_frames(path_to_darks_dir, aq_date, aq_cam, expos_time):
    return dark_frames_list, darks_array

def load_flat_frames(path_to_flats_dir, aq_date, aq_cam, aq_filter, expos_time):
    return flat_frames_list, flats_array

def write_master_bias(bias_array, date="", camera=""):
    return master_bias_as_array

def write_master_dark(darks_array, date="", camera="", exposure=0.):
    return master_dark_as_array, hot_pixels_map

def write_master_flat(darks_array, date="", camera="", obs_filter="", exposure=0.):
    return master_flat_as_array, dead_pixels_map

def calibration(fits_image):
    # Get information from FITS header
    aq_date, aq_hms, aq_cam, aq_filter, expos_time = get_infos_from_image(fits_image)
    
    # Ensure the date can be matched to an observation night D, i.e.. it is either :
    # - D and 12:00:00 <= HH:MM:SS <= 23:59:59
    # - D+1 and 00:00:00 <= HH:MM:SS <= 11:59:59
    # TBD
    