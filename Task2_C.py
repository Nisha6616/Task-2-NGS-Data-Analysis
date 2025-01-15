import vcfpy
import statistics
from scipy.stats import binom

def calculate_median_background(normal_variants.vcf):
    allele_frequencies = []
    vcf_reader = vcfpy.Reader(open(normal_variants.vcf, 'r'))
    for record in vcf_reader:
        if 'AF' in record.INFO:
            allele_frequencies.append(record.INFO['AF'][0])
    
    median_af = statistics.median(allele_frequencies)
    print(f"Median Background Mutation Level: {median_af:.5f}")

calculate_median_background("background_filtered.vcf")

#Required reads per million 

def calculate_required_rpm(median_background, confidence_threshold=0.01):
    required_rpm = confidence_threshold / median_background
    print(f"Required Reads per Million (RPM): {required_rpm:.2f}")

calculate_required_rpm(median_background)

#Confidence levels validation

def confidence_level(variant_reads, total_reads, threshold=0.95):
    p = variant_reads / total_reads
    lower, upper = binom.interval(threshold, total_reads, p, loc=0)
    print(f"95% Confidence Interval: {lower/total_reads:.3f} - {upper/total_reads:.3f}")

