import torch
import torch.nn.functional as F
from itertools import count

ints_str_lst = ["95 85", "85 95", "80 70", "70 65", "60 70"]

# Read ints.
x = []
y = []
for ints_str in ints_str_lst:
    ints = [float(x) for x in ints_str.split()]
    x.append( [ints[0]] )
    y.append( [ints[1]] )
x = torch.tensor(x)
y = torch.tensor(y)
y = y
print("x = ", x)
print("y = ", y)
#print(x.shape)

def poly_desc(W, b):
    """Creates a string description of a polynomial."""
    result = 'y = '
    for i, w in enumerate(W):
        result += '{:+.4f} x^{} '.format(w, len(W) - i)
    result += '{:+.4f}'.format(b[0])
    return result


def get_batch(batch_size=4):
    """Builds a batch i.e. (x, f(x)) pair."""
    random = torch.randperm(len(ints_str_lst))[:batch_size].unsqueeze(1)
    #random = torch.randperm(len(ints_str_lst)).unsqueeze(1)
    #random = torch.tensor(range(batch_size)).unsqueeze(1)
    #print(random.shape)
    #print(random)
    batch_x = torch.gather(x, dim=0, index=random)
    batch_y = torch.gather(y, dim=0, index=random)
    return batch_x, batch_y
#get_batch()


# Define our tiny model.
model = torch.nn.Linear(1, 1, bias=True)
loss = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr = 0.01)

for batch_idx in count(1):
    # Get data
    batch_x, batch_y = get_batch()
    #print("batch_x = ", batch_x)
    #print("batch_y = ", batch_y)

    # Reset gradients
    model.zero_grad()

    #print(model(batch_x))
    #print(batch_y)
    #print(model.parameters())

    # Forward pass
    preds = model(batch_x)
    output = loss(preds, batch_y)
    loss_val = output.item()
    if (batch_idx % 1000) == 0:
        print("{}\t loss: {:+.4f}\t model: {}".format(batch_idx, loss_val, poly_desc(model.weight.view(-1), model.bias)))

    # Backward pass
    output.backward()

    # Apply gradients
    optimizer.step()
    #for param in model.parameters():
    #    param.data.add_(-0.00002 * param.grad.data)

    # Stop criterion
    if loss_val < 1e-3:
        break
    if batch_idx > 50000:
        break

    
print('Loss: {:.6f} after {} batches'.format(loss_val, batch_idx))
print('==> Learned function:\t' + poly_desc(model.weight.view(-1), model.bias))

# Print value for 80.
y = model(torch.tensor([80.0])).item()
print(y)
