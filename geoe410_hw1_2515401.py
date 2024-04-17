from matplotlib import pyplot as plt
from tabulate import tabulate

list_depth = [1000, 1200, 1500, 1750, 2000, 2300,
              2700, 3000, 3500, 3600, 3800, 4000,
              4500, 4600, 4800, 5000]  # m

list_wt_percent = [19.0, 18.1, 16.2, 14.1, 14.4, 10.5,
                   9.2, 18.4, 23.2, 39.6, 42.1, 28.3,
                   41.3, 45.0, 0.0, 0.0]  # %

list_df_percent = [36.1, 54.0, 50.1, 42.3, 48.1, 64.0,
                   47.1, 46.1, 41.1, 21.2, 18.2, 18.3,
                   13.1, 9.2, 0.0, 0.0]  # %

list_sp_percent = [4.2, 1.3, 6.2, 2.2, 1.0, 3.3, 8.2,
                   3.4, 4.1, 1.0, 0.0, 2.1, 1.1, 1.5,
                   0.0, 0.0]  # %

list_fu_percent = [5.4, 2.1, 4.3, 10.1, 6.2, 0.0, 6.1,
                   7.1, 7.4, 11.1, 13.1, 12.2, 13.4,
                   14.1, 100.0, 100.0]  # %
list_va_percent = [28.0, 18.3, 21.0, 23.1, 26.2, 19.1,
                   28.3, 22.0, 21.1, 27.1, 24.4, 35.1,
                   31.1, 28.2, 0.0, 0.0]  # %
list_lt_percent = [6.2, 4.1, 1.0, 5.0, 2.1, 3.1, 1.1,
                   2.0, 1.0, 0.0, 1.1, 2.0, 0.0, 1.0,
                   0.0, 0.0]  # %

list_rs_percent = [1.1, 2.1, 1.2, 3.2, 2.0, 0.0, 0.0,
                   1.0, 2.1, 0.0, 1.1, 2.0, 0.0, 1.0,
                   0.0, 0.0]  # %

plt.subplot(4, 2, 1)
plt.scatter(list_wt_percent, list_depth)
plt.title("Depth versus Wood Tissues Percentage")
plt.xlabel("Origin Percentage, %")
plt.ylabel("Depth, m")
plt.gca().invert_yaxis()
plt.grid(True)


plt.subplot(4, 2, 2)
plt.scatter(list_df_percent, list_depth)
plt.title("Depth versus Dinoflagellites Percentage")
plt.xlabel("Origin Percentage, %")
plt.ylabel("Depth, m")
plt.gca().invert_yaxis()
plt.grid(True)

plt.subplot(4, 2, 3)
plt.scatter(list_sp_percent, list_depth)
plt.title("Depth versus Spores Pollen Percentage")
plt.xlabel("Origin Percentage, %")
plt.ylabel("Depth, m")
plt.gca().invert_yaxis()
plt.grid(True)

plt.subplot(4, 2, 4)
plt.scatter(list_fu_percent, list_depth)
plt.title("Depth versus Fusinite Percentage")
plt.xlabel("Origin Percentage, %")
plt.ylabel("Depth, m")
plt.gca().invert_yaxis()
plt.grid(True)

plt.subplot(4, 2, 5)
plt.scatter(list_va_percent, list_depth)
plt.title("Depth versus Various Algae Percentage")
plt.xlabel("Origin Percentage, %")
plt.ylabel("Depth, m")
plt.gca().invert_yaxis()
plt.grid(True)

plt.subplot(4, 2, 6)
plt.scatter(list_lt_percent, list_depth)
plt.title("Depth versus Leaf Tissue Percentage")
plt.xlabel("Origin Percentage, %")
plt.ylabel("Depth, m")
plt.gca().invert_yaxis()
plt.grid(True)

plt.subplot(4, 2, 7)
plt.scatter(list_rs_percent, list_depth)
plt.title("Depth versus Resins Percentage")
plt.xlabel("Origin Percentage, %")
plt.ylabel("Depth, m")
plt.gca().invert_yaxis()
plt.grid(True)

plt.show()

list_tot = []  # %

for i in range(0, len(list_depth)):
    list_tot.append(round(list_wt_percent[i]+list_df_percent[i]+list_sp_percent[i]+list_fu_percent[i]+list_va_percent[i]+list_lt_percent[i]+list_rs_percent[i], 3))

list_type_1 = []  # %

for i in range(0, len(list_df_percent)):
    type1_tot = list_df_percent[i] + list_va_percent[i]
    list_type_1.append(round(type1_tot, 3))

list_type_2 = []  # %

for i in range(0, len(list_sp_percent)):
    type2_tot = list_sp_percent[i] + list_lt_percent[i] + list_rs_percent[i]
    list_type_2.append(round(type2_tot, 3))

list_type_3 = []  # %

for i in range(0, len(list_wt_percent)):
    type3_tot = list_wt_percent[i]
    list_type_3.append(round(type3_tot, 3))

list_type_4 = []  # %

for i in range(0, len(list_fu_percent)):
    type4_tot = list_fu_percent[i]
    list_type_4.append(round(type4_tot, 3))


plt.subplot(2, 2, 1)
plt.scatter(list_type_1, list_depth, c="blue")
plt.title("Depth versus Type I Kerogen Percentage")
plt.xlabel("Origin Percentage, %")
plt.ylabel("Depth, m")
plt.gca().invert_yaxis()
plt.grid(True)

plt.subplot(2, 2, 2)
plt.scatter(list_type_2, list_depth, c="orange")
plt.title("Depth versus Type II Kerogen Percentage")
plt.xlabel("Origin Percentage, %")
plt.ylabel("Depth, m")
plt.gca().invert_yaxis()
plt.grid(True)

plt.subplot(2, 2, 3)
plt.scatter(list_type_3, list_depth, c="purple")
plt.title("Depth versus Type III Kerogen Percentage")
plt.xlabel("Origin Percentage, %")
plt.ylabel("Depth, m")
plt.gca().invert_yaxis()
plt.grid(True)

plt.subplot(2, 2, 4)
plt.scatter(list_type_4, list_depth, c="green")
plt.title("Depth versus Type IV Kerogen Percentage")
plt.xlabel("Origin Percentage, %")
plt.ylabel("Depth, m")
plt.gca().invert_yaxis()
plt.grid(True)

plt.show()

list_types_data = []

for i in range(0, len(list_depth)):
    list_types_data.append([list_depth[i], list_type_1[i],
                            list_type_2[i], list_type_3[i], list_type_4[i]])

col_name = ["Depth, m", "Type I, %", "Type II, %", "Type III, %", "Type IV, %"]

print(tabulate(list_types_data, headers=col_name, tablefmt="fancy_grid"))

