from django.shortcuts import render, get_object_or_404, redirect
from .models import Board
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import BoardForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages

def board_list(request):
    boards = Board.objects.all()
    # 페이지네이션 설정
    paginator = Paginator(boards, 5)  # 한 페이지당 10개씩 보여주기
    page = request.GET.get('page')

    try:
        boards = paginator.page(page)
    except PageNotAnInteger:
        boards = paginator.page(1)
    except EmptyPage:
        boards = paginator.page(paginator.num_pages)

    context = {
        'boards': boards,
    }
    return render(request, 'board/board_list.html', context)

def board_detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'board/board_detail.html', {'board': board})

@login_required
def board_create(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.author = request.user
            board.save()
            return redirect('board:board_detail', pk=board.pk)
    else:
        form = BoardForm()
    return render(request, 'board/board_edit.html', {'form': form})
 
 
 
@login_required
def board_edit(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if board.author != request.user:
        messages.error(request, "수정권한이 없습니다")
        return redirect('board:board_list')
    
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.author = request.user
            board.save()
            return redirect('board:board_detail', pk=board.pk)
    else:
        form = BoardForm(instance=board)
    return render(request, 'board/board_edit.html', {'form': form})
 
@login_required
@require_POST
def board_delete(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if board.author != request.user:
        messages.error(request, "수정권한이 없습니다.")
        return redirect('board:board_list')
    
    board.delete()
    return redirect('board:board_list')
