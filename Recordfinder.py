total_records=128
compatible_records=10
complete_patches=total_records//compatible_records
incomplete_patches=total_records%compatible_records
print(f"""{complete_patches} complete patches""")
print(f"""{incomplete_patches} incomplete records""")
