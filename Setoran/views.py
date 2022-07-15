from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import RegisterForm, UstadzForm, SetoranForm, MahasantriForm
from .filters import SetoranFilter
from django.contrib import messages
from .decorators import tolakhalaman_ini, ijinkan_pengguna, pilihan_login
from django.contrib.auth.models import Group


def profile_page(request):
    return HttpResponse("<h1>Halaman profile</h1>")


def contact_page(request):
    return HttpResponse("<h1>Halaman contact</h1>")


@tolakhalaman_ini
def loginPage(request):
    formlogin = AuthenticationForm
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cocokan = authenticate(request, username=username, password=password)
        if cocokan is not None:
            login(request, cocokan)
        return redirect('home')
    context = {
        'judul': 'Halaman Login',
        'menu': 'login',
        'tampillogin': formlogin
    }
    return render(request, 'data/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')



# @ijinkan_pengguna(yang_diizinkan=['admin'])
@login_required(login_url='login')
@pilihan_login
def home(request):
    list_ustadz = Ustadz.objects.all()
    total_ust = list_ustadz.count()
    list_mhs = Mahasantri.objects.all()
    total_mhs = list_mhs.count()
    
    list_setoran = Setoran.objects.all()
    # total_orders = list_setoran.count()
    # delivered = list_setoran.filter(status='Delivered').count()
    # pending = list_setoran.filter(status='Pending ').count()

    context = {
        'judul': 'Halaman Home',
        'menu': 'home',
        'ustadz': total_ust,
        'mahasantri': total_mhs,
        
        'setoran': list_setoran,
        # 'data_total_orders': total_orders,
        # 'data_delivered': delivered,

    }
    return render(request, 'data/dashboard.html', context)


# Tambah Ustadz
@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['Admin'])
def registerPage(request):
    formregister = RegisterForm()
    if request.method == 'POST':
        formregister = RegisterForm(request.POST)
        if formregister.is_valid():
            nilaiusername = formregister.cleaned_data.get('username')
            messages.success(request, f'Username Anda adalah {nilaiusername}')
            group_ustadz = formregister.save()
            grup = Group.objects.get(name='ustadz')
            group_ustadz.groups.add(grup)
            Ustadz.objects.create(
                user=group_ustadz,
                name=group_ustadz.username)
            return redirect('login')
    context = {
        'judul': 'Halaman Register',
        'menu': 'register',
        'tampilregister': formregister
    }
    return render(request, 'data/register.html', context)

#@ijinkan_pengguna(yang_diizinkan=['Admin''ustadz'])
@login_required(login_url='login')

def ustad(request):
    list_ustadz = Ustadz.objects.all()

    context = {
        'judul': 'Halaman Ustad',
        'menu': 'ustadz',
        'ustadz': list_ustadz,

    }
    return render(request, 'data/ustad.html', context)


@login_required(login_url='login')

def ustadz(request, pk):
    detailustadz = Ustadz.objects.get(id=pk)
    context = {
        'judul': 'Halaman Konsumen',
        'ustadz': detailustadz,

    }
    return render(request, 'data/ustadz.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['Admin'])
def updateUstad(request, pk):
    updatep = Ustadz.objects.get(id=pk)
    formustd = UstadzForm(instance=updatep)
    if request.method == 'POST':
        formedit = UstadzForm(request.POST, request.FILES, instance=updatep)
        if formedit.is_valid:
            formedit.save()
            return redirect('ustad')
    context = {
        'judul': 'Edit Ustadz',
        'form': formustd,
    }
    return render(request, 'data/ustad_edit_form.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['Admin'])
def deleteUstad(request, pk):
    ustadhapus = Ustadz.objects.get(id=pk)
    if request.method == 'POST':
        ustadhapus.delete()
        return redirect('ustad')
    context = {
        'judul': 'Hapus Data Ustadz',
        'ustadzdelete': ustadhapus,
    }
    return render(request, 'data/delete_ustadz.html', context)

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['Admin'])
def createMahasantri(request):
    formms = MahasantriForm()
    if request.method == 'POST':
        formsimpan = MahasantriForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('mahasantri')
    context = {
        'judul': 'Form Mahasantri',
        'form': formms,
    }
    return render(request, 'data/mahasantri_form.html', context)


@login_required(login_url='login')
def mahasantri(request):
    list_mahasantri = Mahasantri.objects.all()

    context = {
        'judul': 'Halaman Data Mahasantri',
        'menu': 'mahasantri',
        'mahasantri': list_mahasantri,

    }
    return render(request, 'data/mahasantri.html', context)


@ijinkan_pengguna(yang_diizinkan=['Admin'])
@login_required(login_url='login')
def updateMahasantri(request, pk):
    updatep = Mahasantri.objects.get(id=pk)
    formmh = MahasantriForm(instance=updatep)
    if request.method == 'POST':

        formedit = MahasantriForm(request.POST, instance=updatep)
        if formedit.is_valid:
            formedit.save()
            return redirect('mahasantri')
    context = {
        'judul': 'Edit Mahasantri',
        'form': formmh,
    }
    return render(request, 'data/mahasantri_form.html', context)


@ijinkan_pengguna(yang_diizinkan=['Admin'])
@login_required(login_url='login')
def deleteMahasantri(request, pk):
    mahasantrihapus = Mahasantri.objects.get(id=pk)
    if request.method == 'POST':
        mahasantrihapus.delete()
        return redirect('mahasantri')
    context = {
        'judul': 'Hapus Data Mahasantri',
        'mahasantritdelete': mahasantrihapus,
    }
    return render(request, 'data/delete_mahasantri.html', context)


@login_required(login_url='login')
def mhsantri(request, pk):
    detailmhsantri = Mahasantri.objects.get(id=pk)
    setoran_mhsantri = detailmhsantri.setoran_set.all()
    total_mhsantri = setoran_mhsantri.count() / 3 + 4
    filter_setoran = SetoranFilter(request.GET, queryset=setoran_mhsantri)
    setoran_mhsantri = filter_setoran.qs

    halaman_tampil = Paginator(setoran_mhsantri, 3)
    halaman_url = request.GET.get('halaman', 1)
    halaman_setoran = halaman_tampil.get_page(halaman_url)

    if halaman_setoran.has_previous():
        url_previous = f'?halaman={halaman_setoran.previous_page_number()}'
    else:
        url_previous = ''
    if halaman_setoran.has_next():
        url_next = f'?halaman={halaman_setoran.next_page_number()}'
    else:
        url_next = ''
    context = {
        'judul': 'Halaman Detail Mahasantri',
        'mahasantri': detailmhsantri,
        # 'data_order_ustadz': order_ustadz,
        'halaman_setoran_mahasantri': halaman_setoran,
        'data_total_mahasantri': total_mhsantri,
        'filter_data_setoran': filter_setoran,
        'previous': url_previous,
        'next': url_next
    }

    return render(request, 'data/mhsantri.html', context)


@login_required(login_url='login')
def add_kitab_to_setoran(request):
    formsetoran = SetoranForm()
    if request.method == 'POST':
        formsimpan = SetoranForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
        return redirect('mahasantri')
    context = {
        'judul': 'Form Order',
        'form': formsetoran,
    }
    return render(request, 'data/add_setoran.html', context)


@login_required(login_url='login')
def deleteSetoran(request, pk):
    setoranhapus = Setoran.objects.get(id=pk)
    if request.method == 'POST':
        setoranhapus.delete()
        return redirect('mahasantri')
    context = {
        'judul': 'Hapus Data Order',
        'datasetorandelete': setoranhapus,
    }
    return render(request, 'data/delete_setoran.html', context)


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['ustadz'])
def userPage(request):

    context = {

    }
    return render(request, 'data/user.html', context)


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['ustadz'])
def accountSetting(request):
    dataustadz = request.user.ustadz
    form = UstadzForm(instance=dataustadz)
    if request.method == 'POST':
        form = UstadzForm(request.POST, request.FILES, instance=dataustadz)
        if form.is_valid:
            form.save()
            messages.success(request, 'Sukses Mengedit.')
            return redirect()
    context = {
        'menu': 'settings',
        'formustadz': form
    }
    return render(request, 'data/account_setting.html', context)
