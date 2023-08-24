def main():
    females = int(input('Enter the amount of females in class: '))
    males = int(input('Enter the amount of males in class: '))
    total_students = females + males
    m_perc = (males * 100) / total_students
    f_perc = (females * 100) / total_students
    print('The total number of students: \t\t' + str(total_students))
    
    print ('Total percentage of males in class: \t' + format(m_perc, '.2f') +'%')
    print ('Total percentage of females in class: \t' + format(f_perc, '.2f') +'%')
    return m_perc, f_perc


if __name__ == '__main__':
    main()
