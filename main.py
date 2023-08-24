def main():
    females = int(input('Enter the amount of females in class: '))
    males = int(input('Enter the amount of males in class: '))
    total_perc = females + males
    f_perc = (females * 100) / total_perc
    m_perc = (males * 100) / total_perc
    print ('Total percentage of females in class: ' + format(f_perc, '.2f') +'%')
    print ('Total percentage of males in class: ' + format(m_perc, '.2f') +'%')
    return m_perc, f_perc


if __name__ == '__main__':
    main()
